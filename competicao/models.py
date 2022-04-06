from django.db import models


# Create your models here.
class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Competicao(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateTimeField()
    local = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Resultado(models.Model):
    atleta = models.ForeignKey('Atleta', on_delete=models.CASCADE)
    modalidade = models.ForeignKey('Modalidade', on_delete=models.CASCADE)
    competicao = models.ForeignKey('Competicao', on_delete=models.CASCADE)
    resultado = models.FloatField()

    def __str__(self):
        return self.atleta
