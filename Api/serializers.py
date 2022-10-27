
from rest_framework import serializers

from core.models import Produto, User,Cart, CartItem,Order,OrderItem
from rest_framework.serializers import SerializerMethodField
from drf_writable_nested import WritableNestedModelSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','codigo_do_produto','estoque','foto','descricao','preco']




#https://www.django-rest-framework.org/api-guide/relations/
class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
        'nome',
        'email',
        'password'
        ]
        
class CartSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    
    cliente = ClienteSerializer()
    items = serializers.StringRelatedField(source='cart', many=True)
    class Meta:
        model = Cart
        fields = [
        'id',
        'cliente',
        'created_at',
        'updated_at',
        'items'
        ] 
          
class CartItemsSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    
    cart = CartSerializer(many=True)
    produto = ProdutoSerializer(many=True)
    class Meta:
        model = CartItem
        fields = [
        'id',
        'cart',
        'produto',
        'quantidade',
        'created_at',
        'updated_at',
        ] 
        
class OrderSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    
    cliente = ClienteSerializer(many=True)
    order_items = serializers.StringRelatedField(many=True, required=False)
    class Meta:
        model = Order
        fields = [
        'id',
        'cliente',
        'total',
        'created_at',
        'updated_at',
        'order_items'
        ] 
        def create(self, validated_data):
            """Override the creation of Order objects
        Parameters
        ----------
        validated_data: dict
        """
            order = Order.objects.create(**validated_data)
            return order
        
        
class OrderItemSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    
    """Serializer for the OrderItem model."""

    order = OrderSerializer(many=True)
    produto = ProdutoSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = (
            'id', 'order', 'produto', 'quantidade','total','subtotal'
        )