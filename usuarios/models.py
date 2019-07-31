from django.db import models

# Create your models here.


class Usuarios(models.Model):
    nome =  models.CharField('Nome Completo', max_length = 50)
    nome_usuario = models.CharField('Login de Usuario', max_length=30)
    data_inicio  = models.DateField('Data Inicio')
    data_fim = models.DateField('Data Termino')
    setor =  models.CharField('Setor', max_length = 30 )
    ramal = models.DecimalField('Ramal',  max_digits=3, decimal_places=2)

    def __str__ (self):
        return self.nome_usuario