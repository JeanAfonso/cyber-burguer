
from django.urls import path
from core.views import IndexView,MenuView,AboutView,BookView,cart_home,PedidoView,ProdutoListView
from django.urls import path,include

from . import views
urlpatterns = [

    path('',IndexView.as_view(), name='index'),
    path('menu/',MenuView.as_view(), name='menu'),
    path('about/',AboutView.as_view(), name='about'),
    path('book/',BookView.as_view(), name='book'),
    path('carrinho/', cart_home, name='carrinho'),
    #path('car_update/', cart_update, name='update'),
    path('pedido/', PedidoView.as_view(), name='pedido'),
    path('teste/', views.ProdutoListView, name='produtos')

]
