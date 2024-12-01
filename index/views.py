from django.shortcuts import render
from index.models import NomeDaEmpresa, LogoBanner, LadoEsquerdo, LadoDireito, NavBar


def index(request):
    if request.method == 'GET':
        # NavBar
        navbar =NavBar.objects.first()

        # Banne  nome da emprea
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

        return render(request, 'index.html', contexto)

    elif request.method == 'POST':
        pass
