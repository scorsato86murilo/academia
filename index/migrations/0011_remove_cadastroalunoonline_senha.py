# Generated by Django 5.1.3 on 2024-12-30 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_remove_cadastroalunoonline_bairro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastroalunoonline',
            name='senha',
        ),
    ]