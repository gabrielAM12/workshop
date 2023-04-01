from django.db import models

class Supermercados(models.Model):
    nome= models.CharField(max_length=200)
    endereco= models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome= models.CharField(max_length=200)
    preco=models.FloatField()
    codigo= models.CharField(max_length=100)
    quantidade= models.IntegerField()

    def __str__(self):
        return self.nome


class Clientes(models.Model):
    nome= models.CharField(max_length=200)
    cpf=models.CharField(max_length=11)
    endereco= models.CharField(max_length=100)
    telefone= models.CharField(max_length=9)
    email= models.EmailField()

    def __str__(self):
        return self.nome

