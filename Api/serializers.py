
from rest_framework import serializers

from core.models import Produto, Cliente, Endereco, Car

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
        'nome', 
        'codigo_do_produto', 
        'preco','estoque', 
        'foto',
        'descricao']
    

          
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
        'rua',
        'numero', 
        'cep',
        #'created_at',
        #'updated_at'
        ]
        
                       
class CarSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField(many=True)

    class Meta:
        model = Car
        fields = [
        'id',
        'user',
        'get_produtos', 
        'total',
        'observacao',
        #'created_at',
        #'updated_at'
        ]

        # You can extend here to work on `user_object` as required - update etc.



class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    #pedidos = PedidoSerializer()
    class Meta:
        
        model = Cliente
        fields = [
        'nome',
        'sobrenome',
        'email', 
        'telefone',
        'endereco',
        #'pedidos',
        #'created_at',
        #'updated_at'
        ]   
     

