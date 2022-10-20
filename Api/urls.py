
from django.urls import path
from Api.views import ProdutoViewSet,ClienteViewSet,EnderecoViewSet
from django.urls import path,include
from rest_framework import routers
from knox import views as knox_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'Produto', ProdutoViewSet, basename='ProdutoSerializer')
router.register(r'Cliente', ClienteViewSet, basename='ClienteViewSet')
router.register(r'Endereco', EnderecoViewSet, basename='EnderecoViewSet')

urlpatterns = [
    path('api-auth/',  include(router.urls)),
    path('api-auth/token/', TokenObtainPairView.as_view()),
    path('api-auth/refresh/', TokenRefreshView.as_view())
]