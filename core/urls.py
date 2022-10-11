
from django.urls import path
from core.views import IndexView,MenuView,AboutView,BookView,ProdutoViewSet
from django.urls import path,include
from rest_framework import routers





router = routers.DefaultRouter()
router.register(r'Produto', ProdutoViewSet, basename='ProdutoSerializer')


urlpatterns = [

    path('',IndexView.as_view(), name='index'),
    path('/menu/',MenuView.as_view(), name='menu'),
    path('/about/',AboutView.as_view(), name='about'),
    path('/book/',BookView.as_view(), name='book'),
    path('api-auth/',  include(router.urls))

    

    
]
