# Generated by Django 5.1.3 on 2024-12-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_nomedaempresa_delete_nomedampresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_aviso', models.ImageField(upload_to='Banner_index')),
                ('altura', models.IntegerField(default=0)),
                ('largura', models.IntegerField(default=40)),
            ],
        ),
    ]