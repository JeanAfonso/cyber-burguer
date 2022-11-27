from Usuarios.views import UsuarioCreate,UsuarioView,PerfilUpdate
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

    path('cadastro/', UsuarioCreate.as_view() , name='cadastro'),
    path('atualizar/', PerfilUpdate.as_view() , name='atualizar'),
    path('usuario', UsuarioView, name='usuarios'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view( template_name = 'sessao_3/login/login.html'), name='login'),
    
]
