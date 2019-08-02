from django.db import models



class Usuarios (models.Model):
    nome = models.CharField('Nome', max_length=50)
    nome_usuario = models.CharField('Usuário', max_length=30)
    data_inicio = models.DateField('Data Inicio')
    data_fim = models.DateField('Data Final')
    setor = models.CharField('Setor', max_length=20)
    ramal = models.IntegerField('Ramal')



    def __str__(self):
        return self.nome

        
