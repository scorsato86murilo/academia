from django.db import models

class CadastroAluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)  # CPF geralmente tem 11 caracteres numéricos
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua_av = models.CharField(max_length=200)
    celular = models.CharField(max_length=20)  # Celular com DDD (ex: 11 91234-5678)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome
