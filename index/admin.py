from django.contrib import admin
from .models import NomeDaEmpresa, LadoEsquerdo, LadoDireito, NavBar

class NomeDampresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estilo_font', 'cor_titulo', 'fontSize')
    search_fields = ('nome',)
    list_filter = ('estilo_font', 'cor_titulo')
    ordering = ('nome',)

class LadoEsquerdoAdmin(admin.ModelAdmin):
    list_display = ('background', 'titulo', 'titulo_cor', 'titulo_estilo_font', 'titulo_fontSize', 'texto', 'texto_cor', 'texto_estilo_font', 'texto_fontSize')
    search_fields = ('titulo', 'texto')
    list_filter = ('background', 'titulo_cor', 'texto_cor')
    ordering = ('titulo',)

class LadoDireitoAdmin(admin.ModelAdmin):
    list_display = ('background', 'titulo', 'titulo_cor', 'titulo_estilo_font', 'titulo_fontSize', 'texto', 'texto_cor', 'texto_estilo_font', 'texto_fontSize')
    search_fields = ('titulo', 'texto')
    list_filter = ('background', 'titulo_cor', 'texto_cor')
    ordering = ('titulo',)

class NavBarAdmin(admin.ModelAdmin):
    list_display = ('background', 'texto_cor')
    search_fields = ('background', 'texto_cor')
    list_filter = ('background',)
    ordering = ('background',)

# Registrando os modelos no admin
admin.site.register(NomeDaEmpresa, NomeDampresaAdmin)
admin.site.register(LadoEsquerdo, LadoEsquerdoAdmin)
admin.site.register(LadoDireito, LadoDireitoAdmin)
admin.site.register(NavBar, NavBarAdmin)
