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

        
