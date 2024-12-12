# Generated by Django 5.1.3 on 2024-12-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('rua_av', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]
