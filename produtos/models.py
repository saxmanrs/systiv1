from django.db import models


# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50, blank=True )
    descricao = models.CharField('Descrição',max_length=100)
    valor = models.DecimalField('Valor',max_digits=10, decimal_places=2)
    data = models.DateField('Data')
    hora = models.TimeField('Hora')
    imagem = models.ImageField(upload_to='produto_img')

    def __str__(self):
        return self.nome

class Usuarios(models.Model):
    nome =  models.CharField('Nome Completo', max_length = 50)
    nome_usuario = models.CharField('Login de Usuario', max_length=30)
    data_inicio  = models.DateField('Data Inicio')
    data_fim = models.DateField('Data Termino')
    setor =  models.CharField('Setor', max_length = 30 )
    ramal = models.DecimalField('Ramal',  max_digits=3, decimal_places=2)

    def __str__ (self):
        return self.nome_usuario