# Generated by Django 5.1.3 on 2024-12-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_remove_cadastroalunoonline_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroalunoonline',
            name='senha',
            field=models.CharField(default=2, max_length=128),
            preserve_default=False,
        ),
    ]