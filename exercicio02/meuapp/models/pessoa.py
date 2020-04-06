from django.db import models
from .endereco import Endereco

# Create your models here.
class Pessoa(models.Model):
        nome = models.CharField(max_length=30)
        sobrenome = models.CharField(max_length=30)
        email = models.EmailField(max_length=254, default='abc@abc.com')
        telefone = models.IntegerField(default = 1)
        cpd = models.CharField(max_length=11, default='00000000000')
        endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
        numero = models.IntegerField(default=1)