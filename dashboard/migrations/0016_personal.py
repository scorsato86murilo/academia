# Generated by Django 5.1.6 on 2025-03-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_rename_mensagem_nossosprodutos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos-personal')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zap', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
