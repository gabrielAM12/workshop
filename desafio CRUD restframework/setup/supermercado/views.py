from django.shortcuts import render
from rest_framework import viewsets
from .models import Supermercados, Produtos, Clientes
from .serializers import SupermercadoSerializer, ProdutoSerializer, ClienteSerializer

class SupermercadoViewSet(viewsets.ModelViewSet):
    queryset = Supermercados.objects.all()
    serializer_class = SupermercadoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer