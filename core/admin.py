from django.contrib import admin
from core.models import Produto,Cliente,Endereco,Car

class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'codigo_do_produto',
        'preco', 
        'estoque',
        'descricao',
        'created_at',
        'updated_at',
    )
admin.site.register(Produto, ProdutoAdmin)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'rua',
        'numero', 
        'cep',
        'created_at',
        'updated_at',
    )
admin.site.register(Endereco, EnderecoAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_produtos', 
        'cliente',
        'total',
        'observacao',
        'created_at',
        'updated_at',
    )
admin.site.register(Car, CarAdmin)



    
    
class ClienteAdmin(admin.ModelAdmin):
     
    list_display = (
        'nome',
        'sobrenome',
        'email', 
        'telefone',
        'created_at',
        'updated_at',
    )

 
admin.site.register(Cliente, ClienteAdmin)

