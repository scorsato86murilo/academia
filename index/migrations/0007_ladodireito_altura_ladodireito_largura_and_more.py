# Generated by Django 5.1.3 on 2024-12-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_remove_ladoesquerdo_img_lado_direito_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ladodireito',
            name='altura',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ladodireito',
            name='largura',
            field=models.IntegerField(default=40),
        ),
        migrations.AddField(
            model_name='ladoesquerdo',
            name='altura',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ladoesquerdo',
            name='largura',
            field=models.IntegerField(default=40),
        ),
    ]
