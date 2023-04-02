from django.shortcuts import render
from rest_framework import viewsets
from .models import Supermercado, Produto, Cliente
from .serializers import SupermercadoSerializer, ProdutoSerializer, ClienteSerializer

class SupermercadoViewSet(viewsets.ModelViewSet):
    queryset = Supermercado.objects.all()
    serializer_class = SupermercadoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer