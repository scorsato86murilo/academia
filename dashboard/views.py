from django.shortcuts import render
from .models import CadastroAluno
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

            # Verificar se o CPF já existe no banco de dados
            if CadastroAluno.objects.filter(cpf=cpf).exists():
                messages.error(request, 'Erro: CPF já cadastrado!')
                cpf = CadastroAluno.objects.all()
                return render(request, 'dashboard.html', {'cpf': cpf})  # Retorna ao formulário com mensagem de erro

            try:
                # Criar uma instância do modelo CadastroAluno
                aluno = CadastroAluno(
                    nome=nome,
                    cpf=cpf,
                    cidade=cidade,
                    bairro=bairro,
                    rua_av=rua_av,
                    celular=celular,
                    email=email
                )

                # Salvar a instância no banco de dados
                aluno.save()
                messages.success(request, 'Cadastrado com SUCESSO!')
            except Exception as e:
                messages.error(request, f'Erro: {str(e)}')

        # Redirecionar para a página de dashboard com as mensagens
        cpf = CadastroAluno.objects.all()
        return render(request, 'dashboard.html', {'aluno': aluno, 'cpf': cpf})
