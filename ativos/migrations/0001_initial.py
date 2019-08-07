# Generated by Django 2.2.2 on 2019-08-06 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_setor', models.CharField(max_length=30, verbose_name='Nome do Setor')),
            ],
        ),
        migrations.CreateModel(
            name='StatusAtivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_ativo', models.CharField(max_length=10, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAtivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ativo', models.CharField(max_length=30, verbose_name='Tipo Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Ativos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_ativo', models.CharField(max_length=20, verbose_name='Sigla Ativo')),
                ('nome_ativo', models.CharField(max_length=40, verbose_name='Nome Ativo')),
                ('marca_ativo', models.CharField(max_length=30, verbose_name='Marca Ativo')),
                ('setor_ativo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ativos.Setor')),
                ('status_ativo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ativos.StatusAtivo')),
                ('tipo_ativo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ativos.TipoAtivo')),
            ],
        ),
    ]
