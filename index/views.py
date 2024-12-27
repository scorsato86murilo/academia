from django.shortcuts import render

from dashboard.models import Treino
from index.models import NomeDaEmpresa, LogoBanner, LadoEsquerdo, LadoDireito, NavBar


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
    if request.method == 'GET':
        contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto
        return render(request, 'index.html', contexto)

    elif request.method == 'POST':
        # Lógica para o método POST (se necessário)
        pass


def ficha_treino(request):
    # Inicializando o contexto
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
                else:
                    contexto['erro'] = "Treino Exclusivo para alunos!"  # Caso o treino não seja válido

    # Retorna o contexto com os dados do treino selecionado
    return render(request, 'ficha_treino.html', contexto)
