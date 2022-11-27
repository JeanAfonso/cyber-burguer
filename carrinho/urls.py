
from django.urls import path
from carrinho.views import cart_home,cart_update
from django.urls import path,include
app_name = 'cart'

from . import views
urlpatterns = [

    path('', cart_home, name='home'),
    path('car_update/', cart_update, name='update'),
    #path('pedido/', PedidoView.as_view(), name='pedido'),


]
