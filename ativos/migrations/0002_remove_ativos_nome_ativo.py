# Generated by Django 2.2.3 on 2019-08-07 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ativos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativos',
            name='nome_ativo',
        ),
    ]