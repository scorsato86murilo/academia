# Generated by Django 5.1.6 on 2025-02-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_mensalidade_data_vencimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='NossosProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos-nossos-produtos')),
                ('titulo', models.CharField(max_length=255)),
                ('mensagem', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='mensalidade',
            options={'ordering': ['-data_vencimento'], 'verbose_name': 'Mensalidade', 'verbose_name_plural': 'Mensalidades'},
        ),
    ]
