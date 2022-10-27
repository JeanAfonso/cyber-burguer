
from django.urls import path
from Api.views import ProdutoViewSet,ClienteViewSet, CartViewSet,CartItemViewSet,OrderItemViewSet,OrderViewSet
from django.urls import path,include
from rest_framework import routers
from knox import views as knox_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'Produto', ProdutoViewSet, basename='ProdutoSerializer')
router.register(r'Cliente', ClienteViewSet, basename='ClienteViewSet')
router.register(r'cart', CartViewSet, basename='CartViewSet')
router.register(r'CartItem', CartItemViewSet, basename='CartItemViewSet')
router.register(r'orderItem', OrderItemViewSet, basename='OrderItemSerializer')
router.register(r'Order', OrderViewSet, basename='OrderViewSet')


urlpatterns = [
    path('api-auth/',  include(router.urls)),

]