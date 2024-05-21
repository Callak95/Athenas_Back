from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    sexo = models.CharField(max_length=50)