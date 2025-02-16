from django.contrib import admin
from dashboard.models import CadastroAluno, Treino, TreinoAlunoCadastrado, PulicarAcademia, Mensalidade


class CadastroAlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'cidade', 'bairro', 'data_cadastro']  # Exibir 'data_cadastro' na lista
    fields = ['nome', 'cpf', 'cidade', 'bairro', 'rua_av', 'celular', 'email']  # Excluir 'data_cadastro' do formulário de edição

# Registrando o modelo CadastroAluno após a definição da classe Admin
admin.site.register(CadastroAluno, CadastroAlunoAdmin)

# Registrando os outros modelos normalmente
admin.site.register(Treino)
admin.site.register(TreinoAlunoCadastrado)
admin.site.register(PulicarAcademia)
admin.site.register(Mensalidade)
