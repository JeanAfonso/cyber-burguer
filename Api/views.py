from telnetlib import LOGOUT
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import Response
from Api.serializers import ProdutoSerializer,ClienteSerializer,CartSerializer,CartItemsSerializer,OrderSerializer,OrderItemSerializer
from core.models import CartItem, Order, Produto,User,Cart,OrderItem,User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import serializers



class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ClienteSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    @action(methods=['post','put'],detail = True)
    def add_to_cart(self, request,pk=None):
        cart = self.get_object()
        try:
            produto = Produto.objects.get(
                pk = request.data['produto_id']
            )
            quantidade = int(request.data['quantidade'])
        except Exception as e:
            print(e)
            return Response({'status':'fail'})
        
        if produto.estoque <= 0 or produto.estoque - quantidade < 0:
            print("nao existe produto suficiente no estoque")
            return Response({'status': 'fail'})
        
        existe_cart_item = CartItem.objects.filter(cart=cart, produto=produto).first()
        if existe_cart_item:
            existe_cart_item.quantidade += quantidade
            existe_cart_item.save()
            
        else:
            novo_cart_item = CartItem(cart=cart,produto = produto, quantidade= quantidade)
            novo_cart_item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    
    
    @action(methods=['post','put'],detail = True)
    def remove_o_cart(self, request, pk =None):
        
        cart = self.get_object()
        try:
            product = Produto.objects.get(
                pk=request.data['produto_id']
            )
        except Exception as e:
            print(e)
            return Response({'status': 'fail'})

        try:
            cart_item = CartItem.objects.get(cart=cart,product=product)
        except Exception as e:
            print(e)
            return Response({'status': 'fail'})

        # if removing an item where the quantity is 1, remove the cart item
        # completely otherwise decrease the quantity of the cart item
        if cart_item.quantidade == 1:
            cart_item.delete()
        else:
            cart_item.quantidade -= 1
            cart_item.save()

        # return the updated cart to indicate success
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    
    
    
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemsSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        try:
            #atenção --------------------------------------------------------------------------
            purchaser_id = self.request.data['cliente']
            user = User.objects.get(pk = purchaser_id)
        except:
            raise serializers.ValidationError(
                    'usuario nao encontrado'
            )

        cart = user.cart

        for cart_item in cart.CartItem.all():
            if cart_item.produto.estoque - cart_item.quantidade < 0:
                raise serializers.ValidationError(
                    'We do not have enough inventory of ' + str(cart_item.produto.nome) + \
                    'to complete your purchase. Sorry, we will restock soon'
                    )

            # find the order total using the quantity of each cart item and the product's price
        total_aggregated_dict = cart.CartItem.aggregate(total=Sum(F('quantidade')*F('produto_preco'),output_field=FloatField()))

        order_total = round(total_aggregated_dict['total'], 2)
        order = serializer.save(cliente=user, total=order_total)

        order_items = []
        for cart_item in cart.CartItem.all():
            order_items.append(OrderItem(order=order, produto=cart_item.produto, quantidade=cart_item.quantidade))
            # available_inventory should decrement by the appropriate amount
            cart_item.produto.available_inventory -= cart_item.quantidade
            cart_item.produto.save()


        OrderItem.objects.bulk_create(order_items)
            # use clear instead of delete since it removes all objects from the
            # related object set. It doesnot delete the related objects it just
            # disassociates them, which is what we want in order to empty the cart
            # but keep cart items in the db for customer data analysis
        cart.CartItem.clear()
        
    def create(self, request, *args, **kwargs):
        """Override the creation of Order objects.
        Parameters
        ----------
        request: dict
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(url_path="order_history/(?P<customer_id>[0-9])",detail = True)
    def order_history(self, request, customer_id):
        """Return a list of a user's orders.
        Parameters
        ----------
        request: request
        """
        try:
            user = User.objects.get(id=customer_id)

        except:
            # no user was found, so order history cannot be retrieved.
            return Response({'status': 'fail'})

        orders = Order.objects.filter(customer=user)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

        
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

