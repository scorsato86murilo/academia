from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class NomeDaEmpresa(models.Model):
    objects = None
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
    img_lado_direito = models.ImageField(upload_to='img_lado_direito')
    altura = models.IntegerField(default=0)  # Altura da imagem, valor padrão 0
    largura = models.IntegerField(default=40)  # Largura da imagem, valor padrão 40




class NavBar(models.Model):
    background = models.CharField(max_length=30, default='red')  # Cor de fundo
    texto_cor = models.CharField(max_length=30, default='black')  # Cor do texto

    def __str__(self):
        return f"NavBar (Fundo: {self.background}, Texto: {self.texto_cor})"


class LogoBanner(models.Model):
    img_aviso = models.ImageField(upload_to='Banner_index')
    altura = models.IntegerField(default=0)  # Altura da imagem, valor padrão 0
    largura = models.IntegerField(default=40)  # Largura da imagem, valor padrão 40


from django.contrib.auth.models import AbstractBaseUser


class CadastroAlunoOnLine(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    cidade = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)  # Aqui, vamos usar CharField para o hash da senha

    USERNAME_FIELD = 'email'  # Isso torna o email o campo principal para login
    REQUIRED_FIELDS = ['nome', 'celular', 'cidade']  # Campos adicionais obrigatórios

    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)
