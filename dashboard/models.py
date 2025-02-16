from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone


class CadastroAluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)  # CPF geralmente tem 11 caracteres numéricos
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua_av = models.CharField(max_length=200)
    celular = models.CharField(max_length=20)  # Celular com DDD (ex: 11 91234-5678)
    email = models.EmailField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Treino(models.Model):
    treino_masculino_perder_peso = models.TextField()
    treino_masculino_ganho_massa = models.TextField()
    treino_feminino_perder_peso = models.TextField()
    treino_feminino_ganho_massa = models.TextField()
    treino_masculino_atleta = models.TextField()
    treino_feminino_atleta = models.TextField()


class TreinoAlunoCadastrado(models.Model):
    treino_personalizado_aluno = models.TextField()
    aluno_cadastrado = models.ForeignKey(CadastroAluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.treino_personalizado_aluno


class PulicarAcademia(models.Model):
    foto = models.ImageField(upload_to='fotos-publicar-academia', blank=True, null=True)
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Mensalidade(models.Model):
    aluno = models.ForeignKey(CadastroAluno, on_delete=models.CASCADE)  # Relacionamento com o modelo CadastroAluno
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da mensalidade
    data_vencimento = models.DateField()  # Data de vencimento da mensalidade
    data_matricula = models.DateField()  # Data de matrícula, preenchida automaticamente na criação
    descricao = models.TextField(blank=True, null=True)  # Campo opcional para descrição

    def __str__(self):
        return f'Mensalidade de {self.aluno.nome} - {self.valor}'

