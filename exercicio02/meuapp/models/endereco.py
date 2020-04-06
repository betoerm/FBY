from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.IntegerField()