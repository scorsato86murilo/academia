# Generated by Django 5.1.3 on 2024-12-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ladodireito',
            name='titulo_cor',
            field=models.CharField(default='yellow', max_length=30),
        ),
        migrations.AlterField(
            model_name='ladoesquerdo',
            name='background',
            field=models.CharField(default='orange', max_length=30),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='background',
            field=models.CharField(default='red', max_length=30),
        ),
        migrations.AlterField(
            model_name='nomedampresa',
            name='cor_titulo',
            field=models.CharField(default='blue', max_length=30),
        ),
    ]