from django.contrib import admin 
from .models import Supermercado, Cliente, Produto

class SupermercadoAdmin(admin.ModelAdmin):
    list_display= ('nome','endereco')
admin.site.register(Supermercado,SupermercadoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display= ('nome','cpf','endereco','telefone','email')
admin.site.register(Cliente,ClienteAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display= ('nome','preco','codigo','quantidade')
admin.site.register(Produto,ProdutoAdmin)


# Register your models here.
