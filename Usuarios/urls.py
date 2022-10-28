"""

from Usuarios.views import cadastro,UsuarioView
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view( template_name = 'sessao_3/login/login.html'), name='login'),
    
]"""
