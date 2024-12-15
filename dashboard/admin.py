from django.contrib import admin

from dashboard.models import CadastroAluno, Treino, TreinoAlunoCadastrado

# Register your models here.
admin.site.register(CadastroAluno)
admin.site.register(Treino)
admin.site.register(TreinoAlunoCadastrado)