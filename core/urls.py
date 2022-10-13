
from django.urls import path
from core.views import IndexView,MenuView,AboutView,BookView,ProdutoViewSet,ClienteViewSet,EnderecoViewSet,CarViewSet,CadastroView
from django.urls import path,include
from rest_framework import routers





router = routers.DefaultRouter()
router.register(r'Produto', ProdutoViewSet, basename='ProdutoSerializer')
router.register(r'Cliente', ClienteViewSet, basename='ClienteViewSet')
router.register(r'Endereco', EnderecoViewSet, basename='EnderecoViewSet')
router.register(r'Car', CarViewSet, basename='CarViewSet')


urlpatterns = [

    path('',IndexView.as_view(), name='index'),
    path('/menu/',MenuView.as_view(), name='menu'),
    path('/about/',AboutView.as_view(), name='about'),
    path('/book/',BookView.as_view(), name='book'),
    path('api-auth/',  include(router.urls)),
    path('Cadastro/', CadastroView.as_view(), name='cadastro')
    #path('Login/', LoginView.as_view(), name='login' ),

]
