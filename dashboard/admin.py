from django.contrib import admin

from dashboard.models import CadastroAluno, Treino, TreinoAlunoCadastrado, PulicarAcademia

# Register your models here.
admin.site.register(CadastroAluno)
admin.site.register(Treino)
admin.site.register(TreinoAlunoCadastrado)
admin.site.register(PulicarAcademia)