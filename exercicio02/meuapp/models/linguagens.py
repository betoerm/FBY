from django.db import models

class Linguagens(models.Model):
    nome = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)