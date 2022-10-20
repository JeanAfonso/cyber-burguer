import re
from django.views.generic import TemplateView
from requests import request
from core.models import Produto,Cliente,Endereco,Car

#-------------------------------------------------------------------------------
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#-------------------------------------------------------------------------------
from core.forms import ClienteForm, EnderecoForm
class IndexView(TemplateView):
    template_name = 'index.html'
    

class MenuView(TemplateView):
    template_name = 'menu/food.html'
    
class AboutView(TemplateView):
    template_name = 'menu/about.html'
    
class BookView(TemplateView):
    template_name = 'menu/book.html'
    
class CadastroView(request):
    T_user = request.user
    template_name = 'cadastro\cadastro.html'

def cart_home(request):
    cart_obj = Car.objects.get_or_create(request)
    return render(request, "carrinho\carrinho.html", {})
