from django.shortcuts import render, get_object_or_404
from .models import CadastroAluno, Treino
from django.contrib import messages


def dashboard(request):
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

from django.shortcuts import render, redirect
from .models import Treino


def ficha_treino_dash(request):
    # Verifica se existe algum treino no banco de dados
    treino = Treino.objects.first()  # Pega o primeiro objeto, assumindo que deve haver apenas um treino

    if request.method == 'GET':
        # Se não existir nenhum treino, cria um treino em branco
        if treino is None:
            treino = Treino.objects.create(
                treino_masculino_perder_peso='',
                treino_masculino_ganho_massa='',
                treino_masculino_atleta='',
                treino_feminino_perder_peso='',
                treino_feminino_ganho_massa='',
                treino_feminino_atleta=''
            )

        return render(request, 'ficha_treino_dash.html', {'treino': treino})

    elif request.method == 'POST':
        if 'treino_padrao' in request.POST:
            # Pega os dados enviados pelo formulário
            treino_masculino_perder_peso = request.POST.get('treino_masculino_perder_peso')
            treino_masculino_ganho_massa = request.POST.get('treino_masculino_ganho_massa')
            treino_masculino_atleta = request.POST.get('treino_masculino_atleta')
            treino_feminino_perder_peso = request.POST.get('treino_feminino_perder_peso')
            treino_feminino_ganho_massa = request.POST.get('treino_feminino_ganho_massa')
            treino_feminino_atleta = request.POST.get('treino_feminino_atleta')

            # Se já existir um treino no banco de dados, atualiza os campos
            if treino:
                treino.treino_masculino_perder_peso = treino_masculino_perder_peso
                treino.treino_masculino_ganho_massa = treino_masculino_ganho_massa
                treino.treino_masculino_atleta = treino_masculino_atleta
                treino.treino_feminino_perder_peso = treino_feminino_perder_peso
                treino.treino_feminino_ganho_massa = treino_feminino_ganho_massa
                treino.treino_feminino_atleta = treino_feminino_atleta
                messages.success(request, 'Treino cadastrado com SUCESSO!')
                treino.save()  # Salva as alterações no banco de dados
            else:
                # Caso não exista treino, cria um novo
                Treino.objects.create(
                    treino_masculino_perder_peso=treino_masculino_perder_peso,
                    treino_masculino_ganho_massa=treino_masculino_ganho_massa,
                    treino_masculino_atleta=treino_masculino_atleta,
                    treino_feminino_perder_peso=treino_feminino_perder_peso,
                    treino_feminino_ganho_massa=treino_feminino_ganho_massa,
                    treino_feminino_atleta=treino_feminino_atleta,
                )
                messages.success(request, 'Treino cadastrado com SUCESSO!')

            # Após salvar, redireciona para a página de ficha de treino'

        return redirect('ficha_treino_dash')