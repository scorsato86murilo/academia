from django.db import models


class NomeDaEmpresa(models.Model):
    nome = models.CharField(max_length=255, default='Minha Empresa')
    estilo_font = models.CharField(max_length=100, default='Arial')
    cor_titulo = models.CharField(max_length=30, default='blue')
    fontSize = models.IntegerField(default=16)


class LadoEsquerdo(models.Model):
    background = models.CharField(max_length=30, default='orange')
    titulo = models.CharField(max_length=100, default='Título Esquerdo')
    titulo_cor = models.CharField(max_length=30, default='black')
    titulo_estilo_font = models.CharField(max_length=255, default='Arial')
    titulo_fontSize = models.IntegerField(default=18)

    texto = models.TextField(default='Texto do lado esquerdo')
    texto_cor = models.CharField(max_length=30, default='black')
    texto_estilo_font = models.CharField(max_length=255, default='Arial')
    texto_fontSize = models.IntegerField(default=14)


class LadoDireito(models.Model):
    background = models.CharField(max_length=30, default='white')
    titulo = models.CharField(max_length=100, default='Título Direito')
    titulo_cor = models.CharField(max_length=30, default='yellow')
    titulo_estilo_font = models.CharField(max_length=255, default='Arial')
    titulo_fontSize = models.IntegerField(default=18)

    texto = models.TextField(default='Texto do lado direito')
    texto_cor = models.CharField(max_length=30, default='black')
    texto_estilo_font = models.CharField(max_length=255, default='Arial')
    texto_fontSize = models.IntegerField(default=14)


class NavBar(models.Model):
    background = models.CharField(max_length=30, default='red')
    texto_cor = models.CharField(max_length=30, default='black')
