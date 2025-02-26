from datetime import timedelta
from dateutil.relativedelta import relativedelta  # Para calcular a diferença de 1 mês
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import CadastroAluno, Treino, TreinoAlunoCadastrado, PulicarAcademia, Mensalidade
from django.contrib import messages
from django.contrib.auth import logout
from django.utils import timezone
from datetime import date
from django.shortcuts import render
from .models import NossosProdutos

## sempre que criar uma nova def antes do GET este codigo ##
#    # Verificando se o usuário não é superusuário
#    if not request.user.is_superuser:
#        return HttpResponseForbidden('<b>Acesso negado:</b> apenas o <font color="red">superusuário</font> pode '
#                                     'acessar essa página.'


@login_required(login_url='index')
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('<b>Acesso negado:</b> apenas o <font color="red">superusuário</font> pode '
                                     'acessar essa página.')

    aluno = None  # Variável para armazenar o aluno encontrado

    if request.method == 'GET':
        cpf = CadastroAluno.objects.all()
        return render(request, 'dashboard.html', {'cpf': cpf})

    elif request.method == 'POST':

        # Verificar se é uma busca de CPF ou cadastro
        if 'buscar' in request.POST:
            # Buscar o aluno pelo CPF
            cpf = request.POST.get('cpf_pesquisa')  # CPF para pesquisa
            try:
                aluno_cpf = CadastroAluno.objects.get(cpf=cpf)
                messages.success(request, f'Aluno encontrado: {aluno_cpf.nome}')
                # Redirecionar para a página de dashboard com as mensagens
                return render(request, 'dashboard.html', {'aluno_cpf': aluno_cpf})
            except CadastroAluno.DoesNotExist:
                aluno_cpf = None
                messages.error(request, 'Aluno não encontrado com esse CPF.')
                # Redirecionar para a página de dashboard com as mensagens
                cpf = CadastroAluno.objects.all()
                return render(request, 'dashboard.html', {'aluno_cpf': aluno_cpf, 'cpf': cpf})

        elif 'cadastrar' in request.POST:
            # Obter os dados do formulário de cadastro
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            cidade = request.POST.get('cidade')
            bairro = request.POST.get('bairro')
            rua_av = request.POST.get('rua_av')
            celular = request.POST.get('celular')
            email = request.POST.get('email')
            id = request.POST.get('id')

            # Verificar se o CPF já existe no banco de dados
            if CadastroAluno.objects.filter(cpf=cpf).exists() and not id:
                messages.error(request, 'Erro: CPF já cadastrado!')
                cpf = CadastroAluno.objects.all()
                return render(request, 'dashboard.html', {'cpf': cpf})  # Retorna ao formulário com mensagem de erro

            try:
                if id:  # é verdade que tem id?
                    # Atualizando o aluno existente
                    aluno = get_object_or_404(CadastroAluno, id=id)
                    aluno.nome = nome
                    aluno.cpf = cpf
                    aluno.cidade = cidade
                    aluno.bairro = bairro
                    aluno.rua_av = rua_av
                    aluno.celular = celular
                    aluno.email = email

                    aluno.save()  # Salva as alterações
                    messages.success(request, 'Aluno atualizado com SUCESSO!')
                else:  # se não tem id entao entra aqui
                    # Criar uma instância do modelo CadastroAluno
                    aluno = CadastroAluno(
                        nome=nome,
                        cpf=cpf,
                        cidade=cidade,
                        bairro=bairro,
                        rua_av=rua_av,
                        celular=celular,
                        email=email,
                    )
                    aluno.save()  # Salvar a instância no banco de dados
                    messages.success(request, 'Cadastrado com SUCESSO!')
            except Exception as e:
                messages.error(request, f'Erro: {str(e)}')

        # Redirecionar para a página de dashboard com as mensagens
        cpf = CadastroAluno.objects.all()
        return render(request, 'dashboard.html', {'aluno': aluno, 'cpf': cpf})


@login_required(login_url='index')
def ficha_treino_dash(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('<b>Acesso negado:</b> apenas o <font color="red">superusuário</font> pode '
                                     'acessar essa página.')

    aluno_c = None  # Inicializa a variável como None para evitar o erro UnboundLocalError
    treino = Treino.objects.first()


    if request.method == 'GET':
        # Se não existir treino, cria um novo
        if not treino:
            treino = Treino.objects.create(
                treino_masculino_perder_peso='treino_masculino_perder_peso',
                treino_masculino_ganho_massa='treino_masculino_ganho_massa',
                treino_masculino_atleta='treino_masculino_atleta',
                treino_feminino_perder_peso='treino_feminino_perder_peso',
                treino_feminino_ganho_massa='treino_feminino_ganho_massa',
                treino_feminino_atleta='treino_feminino_atleta'
            )

        return render(request, 'ficha_treino_dash.html',
                      {'treino': treino, 'aluno_c': aluno_c})

    if request.method == 'POST':
        treino_personalizado = None  # ou algum valor padrão que você deseja
        # Se for o 'treino_padrao' ou 'treino_aluno_cadastrado'
        if 'treino_padrao_btn' in request.POST or 'treino_aluno_cadastrado' in request.POST:
            # Para treino padrão
            if 'treino_padrao_btn' in request.POST:
                treino_masculino_perder_peso = request.POST.get('treino_masculino_perder_peso')
                treino_masculino_ganho_massa = request.POST.get('treino_masculino_ganho_massa')
                treino_masculino_atleta = request.POST.get('treino_masculino_atleta')
                treino_feminino_perder_peso = request.POST.get('treino_feminino_perder_peso')
                treino_feminino_ganho_massa = request.POST.get('treino_feminino_ganho_massa')
                treino_feminino_atleta = request.POST.get('treino_feminino_atleta')

                # Validação para os campos de treino
                if not all([treino_masculino_perder_peso, treino_masculino_ganho_massa, treino_masculino_atleta,
                            treino_feminino_perder_peso, treino_feminino_ganho_massa, treino_feminino_atleta]):
                    messages.error(request, 'Todos os campos de treino devem ser preenchidos!')
                    return redirect('ficha_treino_dash')

                # Atualiza ou cria o treino padrão
                if treino:
                    treino.treino_masculino_perder_peso = treino_masculino_perder_peso
                    treino.treino_masculino_ganho_massa = treino_masculino_ganho_massa
                    treino.treino_masculino_atleta = treino_masculino_atleta
                    treino.treino_feminino_perder_peso = treino_feminino_perder_peso
                    treino.treino_feminino_ganho_massa = treino_feminino_ganho_massa
                    treino.treino_feminino_atleta = treino_feminino_atleta
                    treino.save()
                    messages.success(request, 'Treino padrão atualizado com SUCESSO!')
                else:
                    Treino.objects.create(
                        treino_masculino_perder_peso=treino_masculino_perder_peso,
                        treino_masculino_ganho_massa=treino_masculino_ganho_massa,
                        treino_masculino_atleta=treino_masculino_atleta,
                        treino_feminino_perder_peso=treino_feminino_perder_peso,
                        treino_feminino_ganho_massa=treino_feminino_ganho_massa,
                        treino_feminino_atleta=treino_feminino_atleta
                    )
                    messages.success(request, 'Treino padrão cadastrado com SUCESSO!')

        # Para treino personalizado
        if 'treino_aluno_cadastrado_btn' in request.POST:
            treino_aluno_cadastrado = request.POST.get('treino_aluno_cadastrado')
            treino_id = request.POST.get('treino_aluno_cadastrado_id')  # Obtém o ID do treino


            # Se não for fornecido um treino, define o valor padrão
            if treino_aluno_cadastrado == '':
                treino_aluno_cadastrado = "Sem cadastro de treino personalizado"

            if treino_id:  # Se o ID for fornecido, significa que é uma atualização
                try:
                    # Busca o treino personalizado pelo ID
                    treino_atualizar = TreinoAlunoCadastrado.objects.get(id=treino_id)

                    # Atualiza o campo com o treino personalizado enviado
                    treino_atualizar.treino_personalizado_aluno = treino_aluno_cadastrado
                    treino_atualizar.save()  # Salva as alterações

                    # Busca o aluno associado a este treino
                    aluno = CadastroAluno.objects.get(id=treino_atualizar.aluno_cadastrado.id)

                    # Exibe a mensagem de sucesso com o nome do aluno
                    messages.success(request,
                                     f'Treino de {aluno.nome}  personalizado atualizado com SUCESSO!')

                except TreinoAlunoCadastrado.DoesNotExist:
                    messages.error(request, 'Erro: Treino personalizado não encontrado!')
                except CadastroAluno.DoesNotExist:
                    messages.error(request, 'Erro: Aluno relacionado não encontrado!')

            else:
                # Se não houver ID, cria um novo treino personalizado
                novo_treino = TreinoAlunoCadastrado(treino_personalizado_aluno=treino_aluno_cadastrado)
                novo_treino.save()  # Salva o novo treino no banco de dados
                messages.success(request, 'Treino personalizado cadastrado com SUCESSO!')

            # Redireciona de volta ao dashboard ou a outra página relevante
            return redirect('ficha_treino_dash')

        if 'cpf_buscar_btn' in request.POST:
            cpf_buscar = request.POST.get('cpf_buscar')
            print(f'Recebeu CPF: {cpf_buscar}')

            if cpf_buscar:
                try:
                    # Tenta buscar o aluno pelo CPF
                    aluno_c = CadastroAluno.objects.get(cpf=cpf_buscar)
                    messages.success(request, f'Aluno encontrado: {aluno_c.nome}')
                    print(aluno_c)

                    # Busca o treino personalizado do aluno
                    treino_personalizado = TreinoAlunoCadastrado.objects.filter(aluno_cadastrado=aluno_c).first()

                    # Caso não encontre treino personalizado, cria um novo treino personalizado
                    if not treino_personalizado:
                        # Criar um novo objeto de treino personalizado, se necessário
                        treino_personalizado = TreinoAlunoCadastrado.objects.create(
                            treino_personalizado_aluno="Sem treino personalizado",
                            aluno_cadastrado=aluno_c
                        )
                        messages.success(request, 'Crie pela primeira vez um treino para este aluno.')

                except CadastroAluno.DoesNotExist:
                    # Caso não encontre o aluno
                    messages.error(request, 'Erro: Aluno não encontrado!')

                except Exception as e:
                    # Caso ocorra algum outro erro
                    messages.error(request, f'Ocorreu um erro inesperado: {str(e)}')

        # Retorna o render com o treino e o aluno (aluno_c) se encontrado
        return render(request, 'ficha_treino_dash.html', {
            'treino': treino,  # Certifique-se de que a variável 'treino' foi definida antes
            'treino_aluno_cadastrado': treino_personalizado,
            'aluno_c': aluno_c,  # Passando a variável aluno_c para o template
        })


@login_required(login_url='index')
def academia_dash(request):
    # Obtendo todos os objetos e invertendo a ordem pela data de publicação
    objeto_academia = PulicarAcademia.objects.all().order_by('-data_publicacao')[:20]# se mudas esse 20 recomendo que mude la
                                                                                # no index (academia)
    # Verificando se o usuário não é superusuário
    if not request.user.is_superuser:
        return HttpResponseForbidden('<b>Acesso negado:</b> apenas o <font color="red">superusuário</font> pode '
                                     'acessar essa página.')

    if request.method == 'GET':
        # Retorna a página com todos os objetos de academia
        return render(request, 'academia_dash.html', {'objeto_academia': objeto_academia})

    elif request.method == 'POST':
        if 'publicar' in request.POST:
            # Obtendo os dados do formulário
            img = request.FILES.get('img')  # Usando request.FILES para arquivos
            titulo = request.POST.get('titulo')
            msg = request.POST.get('msg')

            try:
                # Criando uma instância do modelo e atribuindo os valores
                salvar = PulicarAcademia(
                    foto=img,
                    titulo=titulo,
                    mensagem=msg
                )

                # Salvando o objeto no banco de dados
                salvar.save()

                # Mensagem de sucesso
                messages.success(request, 'Salvo com sucesso!')

                # Redireciona para a mesma página após o POST
                return redirect('academia_dash')

            except Exception as e:
                messages.error(request, f'Erro ao tentar salvar: {str(e)}')

        # Redireciona para a página com a lista de objetos de academia
        return render(request, 'academia_dash.html', {'objeto_academia': objeto_academia})


@login_required(login_url='index')
def mensalidades(request):
    # Verificando se o usuário não é superusuário
    if not request.user.is_superuser:
        return HttpResponseForbidden(
            '<b>Acesso negado:</b> apenas o <font color="red">superusuário</font> pode acessar essa página.')

    if request.method == 'GET':
        return render(request, 'mensalidade.html')

    if request.method == 'POST':
        if 'procurar' in request.POST:
            cpf_buscar = request.POST.get('cpf_buscar')
            print(f"CPF buscado: {cpf_buscar}")

            # Verifica se o CPF foi passado corretamente
            if not cpf_buscar or len(cpf_buscar) != 11:
                messages.error(request, 'Por favor, forneça um CPF válido com 11 dígitos.')
                return render(request, 'mensalidade.html')

            try:
                # Verificando se o aluno existe
                alunos_cpf = CadastroAluno.objects.filter(cpf=cpf_buscar)
                print(f"Alunos encontrados: {alunos_cpf}")

                if alunos_cpf.exists():
                    # Buscar as mensalidades do aluno
                    mensalidades = Mensalidade.objects.filter(aluno=alunos_cpf.first()).order_by('-data_matricula')

                    # Inicializando a variável mensalidade_em_dia antes do loop
                    mensalidade_em_dia = None

                    # Verificando e exibindo a data de vencimento de cada mensalidade
                    for mensalidade in mensalidades:
                        print(f"Mensalidade: {mensalidade}, Data de Vencimento: {mensalidade.data_vencimento}")

                        # Comparando a data de vencimento com a data atual
                        data_atual = timezone.now().date()  # Pega a data atual sem hora
                        data_vencimento = mensalidade.data_vencimento


                        # Substituindo a data_atual com uma data manual para teste
                        # data_atual_teste = date(2025, 3, 19)  # Data manual (ano, mês, dia)

                        # Verificando se a mensalidade está 1 mês atrasada
                        # data_atual
                        if data_vencimento < data_atual:
                            # Calculando a diferença de um mês
                            diff = relativedelta(data_atual, data_vencimento)

                            # Verifica se a diferença é de 1 mês
                            if diff.months == 1 and diff.years == 0:
                                print(f"A mensalidade de {mensalidade.aluno.nome} está +1 mês atrasada.")
                                mensalidade_em_dia = f'A mensalidade de {mensalidade.aluno.nome}: ESTÁ +1 MÊS ATRASADA.'
                                cor = 1 # text-bg-danger
                            else:
                                print(f"A mensalidade de {mensalidade.aluno.nome} ESTÁ atrasada.")
                                mensalidade_em_dia = f'A mensalidade de {mensalidade.aluno.nome}: ESTÁ atrasada.'
                                cor = 2 # text-bg-warning
                        else:
                            print(f"A mensalidade de {mensalidade.aluno.nome} Tudo OK, não está vencida.")
                            mensalidade_em_dia = f'A mensalidade de {mensalidade.aluno.nome}: Tudo OK!'
                            cor = 3 # text-bg-success

                    # Se a variável mensalidade_em_dia não for alterada, define um valor padrão
                    if mensalidade_em_dia is None:
                        mensalidade_em_dia = "Nenhuma mensalidade encontrada ou condições não atendidas."
                        cor = 4 # text-bg-secondary

                    messages.success(request, 'Aluno encontrado com SUCESSO!')
                    return render(request, 'mensalidade.html', {
                        'alunos': alunos_cpf,
                        'mensalidades': mensalidades,
                        'mensalidade_em_dia': mensalidade_em_dia,  # Passando a variável para o template
                        'cor': cor,

                    })

                else:
                    messages.error(request, 'Aluno não encontrado com esse CPF.')
                    return render(request, 'mensalidade.html')

            except Exception as e:
                print(f"Erro ao buscar aluno: {e}")
                messages.error(request, 'Ocorreu um erro ao tentar buscar o aluno.')
                return render(request, 'mensalidade.html')

        if 'situacao_btn' in request.POST:
            print('botão -> situacao_btn')

            valor_mensal = request.POST.get('valor_mensal')
            descricao = request.POST.get('descricao')
            cpf_aluno = request.POST.get('cpf_aluno')  # Pegando o CPF do aluno enviado pelo formulário
            print(cpf_aluno)

            try:
                # Buscar o aluno com o CPF fornecido
                aluno = CadastroAluno.objects.get(cpf__exact=cpf_aluno)  # Garantir que o aluno seja único

                # Validar o valor da mensalidade
                if not valor_mensal:
                    messages.error(request, 'Por favor, forneça um valor de mensalidade.')
                    return render(request, 'mensalidade.html')

                # Criar a nova mensalidade
                salvar_mensalidades = Mensalidade(
                    aluno=aluno,  # Usando o objeto aluno encontrado
                    valor=valor_mensal,
                    data_matricula=timezone.now().date(),  # Preenche com a data atual
                    descricao=descricao,
                )
                salvar_mensalidades.save()
                messages.success(request, 'SUCESSO! Mensalidade atualizada com SUCESSO!')
            except CadastroAluno.DoesNotExist:
                messages.error(request, 'Aluno não encontrado com esse CPF.')
            except Exception as e:
                print(f"Erro ao salvar mensalidade: {e}")
                messages.error(request, 'ERRO no sistema (Erro ao salvar a mensalidade).')

    # ultima saida da função
    return render(request, 'mensalidade.html')


def nossos_produtos(request):
    produtos = NossosProdutos.objects.all()
    if request.method == 'GET':

        return render(request, 'nossos_produtos.html', {
            'produtos': produtos
        })


def nossos_produtos(request):
    if request.method == 'GET':
        produtos = NossosProdutos.objects.all().order_by('-data_publicacao')
        return render(request, 'nossos_produtos.html', {'produtos': produtos})

    elif request.method == 'POST':
        if 'btn-salvar-produto' in request.POST:
            imagem = request.FILES.get('imagem')
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            valor = request.POST.get('valor')

            try:
                novo_produto = NossosProdutos(
                    foto=imagem,
                    titulo=titulo,
                    descricao=descricao,
                    valor=valor
                )
                novo_produto.save()
                messages.success(request, 'Produto adicionado com sucesso!')

            except:
                messages.error(request, 'Ocorreu um erro ao tentar salvar este produto.')

    # Após salvar, redireciona para a página de produtos com os produtos atualizados
    # Redireciona para a página de produtos no caso de qualquer outro caso
    return redirect('nossos_produtos')


def deleta_obj_academia(request, id):
    if request.method == 'POST':

        try:
            # Obtém o objeto com o ID especificado ou retorna um erro 404 se não encontrado
            item = get_object_or_404(PulicarAcademia, id=id)
            # Deleta o objeto
            item.delete()

        except:
            messages.error(request, 'Não foi possivel deletar, Tente outra vez.')

    return redirect('academia_dash')

def logout_view(request):
    logout(request)
    messages.error(request, 'DESLOGADO com sucesso!')
    return redirect('index')
