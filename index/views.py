from django.contrib.auth import logout, authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # Usado para criar a senha com hash
from django.contrib.auth.models import User
from dashboard.models import Treino, CadastroAluno, TreinoAlunoCadastrado
from index.models import NomeDaEmpresa, LogoBanner, LadoEsquerdo, LadoDireito, NavBar
from django.contrib import messages


def CoresNavBar():
    # NavBar
    navbar = NavBar.objects.first()

    # Banner e nome da empresa
    nome_empresa = NomeDaEmpresa.objects.first()
    banner = LogoBanner.objects.first()

    # Lado esquerdo e direito
    lado_esquerdo = LadoEsquerdo.objects.first()
    lado_direito = LadoDireito.objects.first()

    contexto = {
        'nome_empresa': nome_empresa,
        'banner': banner,
        'lado_esquerdo': lado_esquerdo,
        'lado_direito': lado_direito,
        'navbar': navbar,
    }

    return contexto  # Retorna o contexto para ser usado nas views


def index(request):
    User = get_user_model()
    # Verifica se já existe um superusuário com o nome 'admin'
    if not User.objects.filter(username='admin').exists():
        try:
            # Cria o superusuário
            User.objects.create_superuser(
                username='adminadmin',
                email='admin@example.com',
                password='adminpassword'
            )
            print("Superuser created successfully!")
        except IntegrityError:
            # Se ocorrer erro de integridade (por exemplo, se o nome de usuário já existir)
            print("Error: A superuser with the username 'admin' already exists.")
    else:
        print("Superuser with username 'admin' already exists. No action taken.")

        contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto

    if request.method == 'GET':
        contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto
        return render(request, 'index.html', contexto)

    elif request.method == 'POST':
        # Lógica para o método POST (se necessário)
        pass

@login_required(login_url='/cadastro_login_/')
def ficha_treino(request):
    contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto base
    treino_selecionado = None  # Variável para armazenar o treino selecionado

    # Lógica para o GET
    if request.method == 'GET':
        return render(request, 'ficha_treino.html', contexto)

    # Lógica para o POST
    elif request.method == 'POST':
        # Consultando o primeiro treino do banco de dados
        treino_s = Treino.objects.first()  # Você pode melhorar isso dependendo da sua lógica de dados

        # Garantindo que há um treino no banco
        if treino_s:
            treino_masculino_perder_peso = treino_s.treino_masculino_perder_peso
            treino_masculino_ganho_massa = treino_s.treino_masculino_ganho_massa
            treino_feminino_perder_peso = treino_s.treino_feminino_perder_peso
            treino_feminino_ganho_massa = treino_s.treino_feminino_ganho_massa
            treino_masculino_atleta = treino_s.treino_masculino_atleta
            treino_feminino_atleta = treino_s.treino_feminino_atleta

            # Verificando se o botão foi pressionado e capturando a seleção do treino
            if 'selecione_treino_btn' in request.POST:
                treino_selecionado = request.POST.get('treino')
                print(f"Treino Selecionado: {treino_selecionado}")  # Apenas para depuração

                # Associando o treino selecionado ao contexto
                if treino_selecionado == 'masculino_perder_peso':
                    contexto['treino'] = treino_masculino_perder_peso
                elif treino_selecionado == 'masculino_ganho_massa':
                    contexto['treino'] = treino_masculino_ganho_massa
                elif treino_selecionado == 'feminino_perder_peso':
                    contexto['treino'] = treino_feminino_perder_peso
                elif treino_selecionado == 'feminino_ganho_massa':
                    contexto['treino'] = treino_feminino_ganho_massa
                elif treino_selecionado == 'masculino_atleta':
                    contexto['treino'] = treino_masculino_atleta
                elif treino_selecionado == 'feminino_atleta':
                    contexto['treino'] = treino_feminino_atleta
                elif treino_selecionado == 'x':
                    contexto['treino'] = "Selecione um treino válido!"
                    messages.error(request, 'Selecione um treino válido!')
                else:
                    contexto['treino'] = "Treino Exclusivo para alunos"

            # Verificando se o botão foi pressionado e capturando a 'buscar treino pelo CPF'
            if 'buscar_treino_btn' in request.POST:
                html_cpf = request.POST.get('cpf')
                print(html_cpf)

                # Buscar aluno pelo CPF no banco de dados
                try:
                    aluno = CadastroAluno.objects.get(cpf=html_cpf)  # Buscar aluno pelo CPF
                    print(f'Aluno encontrado: {aluno.nome}')  # Exemplo de como usar a informação do aluno

                    # Buscar treino associado ao aluno
                    treino = TreinoAlunoCadastrado.objects.get(aluno_cadastrado=aluno)  # Buscar treino do aluno
                    print(f'Treino encontrado: {treino.treino_personalizado_aluno}')  # Exibir o treino do aluno

                    # Aqui você pode fazer o que for necessário com o treino encontrado
                    # Retorne os dados do treino ou continue a lógica necessária

                    contexto['aluno'] = aluno  # Passando o aluno para o contexto
                    contexto['treino'] = treino.treino_personalizado_aluno  # Passando o treino personalizado para o contexto

                except CadastroAluno.DoesNotExist:
                    print("Aluno não encontrado com o CPF informado.")
                    messages.error(request, "Aluno não encontrado com o CPF informado.")
                except TreinoAlunoCadastrado.DoesNotExist:
                    print("Treino não encontrado para o aluno com o CPF informado.")
                    messages.error(request, "Treino não encontrado para o aluno com o CPF informado.")

    # Retorna o contexto com os dados do treino selecionado
    return render(request, 'ficha_treino.html', contexto)


def login_(request):
    contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto
    if request.method == 'GET':
        return render(request, 'cadastro_login.html', contexto)

    elif request.method == 'POST':
        username = request.POST.get('nome')  # Nome do usuário (será o email)
        password = request.POST.get('senha')  # Senha (remoção de espaços)
        # Autentica o usuário
        user = authenticate(username=username, password=password)

        if user is not None:
            # Se a autenticação foi bem-sucedida, faz login do usuário
            login(request, user)
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect('ficha_treino')  # Redireciona para a plataforma após login

        else:
            # Se a autenticação falhar, retorna à página de cadastro ou exibe uma mensagem de erro
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente ou cadastre-se.')
            return redirect('cadastro_login_')

    return render(request, 'cadastro_login.html', contexto)


def cadastro_login_(request):
    contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto
    if request.method == 'GET':
        return render(request, 'cadastro.html', contexto)

    if request.method == 'POST':
        # Obtendo dados do formulário
        username = request.POST.get('nome')  # Nome do usuário (será o email)
        email = request.POST.get('email')  # E-mail
        password = request.POST.get('senha')  # Senha (remoção de espaços)
        conf_senha = request.POST.get('conf_senha')  # Confirmação da senha (remoção de espaços)

        # Verificar se as senhas coincidem
        if password != conf_senha:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'cadastro.html', contexto)

        # Verificar se o nome foi preenchido
        if not username:
            messages.error(request, 'O nome é obrigatório!')
            return render(request, 'cadastro.html', contexto)

        # Verificar se o email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return render(request, 'cadastro.html', contexto)

        # Verificar se o username já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe!')
            return render(request, 'cadastro.html', contexto)

        # Verificar se todos os campos foram preenchidos >> pra garantir que foi preechido
        if not username or not password or not email:
            messages.error(request, 'Preencha todos os campos!')
            return render(request, 'cadastro.html', contexto)

        try:
            # Criar o usuário se as verificações passarem
            user = User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login_')

        except:
            messages.error(request, 'Erro ao criar o usuário. Tente novamente.')
            return render(request, 'cadastro.html', contexto)

    return render(request, 'cadastro.html', contexto)


def logout_view(request):
    logout(request)
    messages.success(request, 'DESLOGADO com sucesso!')
    return redirect('index')
