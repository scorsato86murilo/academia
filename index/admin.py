from django.contrib import admin
from .models import NomeDaEmpresa, LadoEsquerdo, LadoDireito, NavBar, LogoBanner, CadastroAlunoOnLine

# Registrando os modelos no admin
admin.site.register(NomeDaEmpresa)
admin.site.register(LadoEsquerdo)
admin.site.register(LadoDireito)
admin.site.register(NavBar)
admin.site.register(LogoBanner)
admin.site.register(CadastroAlunoOnLine)
