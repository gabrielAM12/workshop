from django.contrib import admin 
from .models import Supermercados, Clientes, Produtos

class SupermercadoAdmin(admin.ModelAdmin):
    list_display= ('nome','endereco')
admin.site.register(Supermercados,SupermercadoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display= ('nome','cpf','endereco','telefone','email')
admin.site.register(Clientes,ClienteAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display= ('nome','preco','codigo','quantidade')
admin.site.register(Produtos,ProdutoAdmin)


# Register your models here.
