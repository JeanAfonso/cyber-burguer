from django.contrib import admin
from core.models import Produto,Cliente,Endereco,Pedido

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


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'sobrenome',
        'email', 
        'telefone',
        'endereco',
        'created_at',
        'updated_at',
    )
admin.site.register(Cliente, ClienteAdmin)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'rua',
        'numero', 
        'cep',
        'created_at',
        'updated_at',
    )
admin.site.register(Endereco, EnderecoAdmin)


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status_pedido',
        'observacao',
        'get_produtos', 
        'cliente',
        'total',
        'created_at',
        'updated_at',
    )
admin.site.register(Pedido, PedidoAdmin)