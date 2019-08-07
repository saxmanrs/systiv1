from django.db import models

# Create your models here.

class Setor(models.Model):
    nome_setor = models.CharField('Nome do Setor', max_length=30)
    
    def __str__(self):
        return self.nome_setor

class StatusAtivo(models.Model):
    status_ativo = models.CharField('Status', max_length=10)

    def __str__(self):
        return self.status_ativo

class TipoAtivo(models.Model):
    tipo_ativo = models.CharField('Tipo Ativo', max_length=30)

    def __str__(self):
            return self.tipo_ativo


class Ativos(models.Model):
    sigla_ativo = models.CharField('Sigla Ativo', max_length=20)
    tipo_ativo  = models.OneToOneField(TipoAtivo, null=True,blank=True, on_delete=models.CASCADE)
    marca_ativo = models.CharField('Marca Ativo', max_length=30)
    setor_ativo = models.OneToOneField(Setor, null=True,blank=True, on_delete=models.CASCADE)
    status_ativo = models.OneToOneField(StatusAtivo,null=True,blank=True, on_delete=models.CASCADE)

    def __str__ (self):
        return self.sigla_ativo