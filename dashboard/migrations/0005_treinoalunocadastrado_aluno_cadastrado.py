# Generated by Django 5.1.3 on 2024-12-18 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_treinoalunocadastrado'),
    ]

    operations = [
        migrations.AddField(
            model_name='treinoalunocadastrado',
            name='aluno_cadastrado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.cadastroaluno'),
            preserve_default=False,
        ),
    ]
