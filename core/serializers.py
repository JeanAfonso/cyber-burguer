
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
    
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
        'nome',
        'sobrenome',
        'email', 
        'telefone',
        'endereco',
        'created_at',
        'updated_at']
        
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
        'rua',
        'numero', 
        'cep',
        'created_at',
        'updated_at']

        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
        'id',
        'get_produtos', 
        'cliente',
        'total',
        'observacao',
        'created_at',
        'updated_at'
        ]

