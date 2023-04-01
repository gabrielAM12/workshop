from rest_framework import serializers
from .models import Supermercados, Produtos, Clientes


class SupermercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermercados
        fields = ['nome', 'endereco']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco','codigo','quantidade']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['nome', 'cpf','endereco','telefone','email']
