from django.shortcuts import render
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
    if request.method == 'GET':
        contexto = CoresNavBar()  # Chama a função CoresNavBar para obter o contexto
        return render(request, 'ficha_treino.html', contexto)

    elif request.method == 'POST':
        pass
