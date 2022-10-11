
from rest_framework import serializers

from core.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['Nome', 'Codigo de produto', 'Preço', 'Quantidade em Estoque']
        
