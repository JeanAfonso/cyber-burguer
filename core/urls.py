
from django.urls import path
from core.views import IndexView,MenuView,AboutView,BookView,CadastroView,cart_home
from django.urls import path,include

urlpatterns = [

    path('',IndexView.as_view(), name='index'),
    path('menu/',MenuView.as_view(), name='menu'),
    path('about/',AboutView.as_view(), name='about'),
    path('book/',BookView.as_view(), name='book'),
    path('cart/', cart_home, name='cart'),
    path('cadastro/', CadastroView.as_view(), name='cadastro')

]
