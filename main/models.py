from django.db import models

# Create your models here.
class Carro (models.Model):
    nome = models.CharField(max_length=10)
    marca = models.CharField(max_length=10)
    ano = models.BigIntegerField()
    cor =models.CharField(max_length=10)
    
    def __str__(self):
       return self.nome
   