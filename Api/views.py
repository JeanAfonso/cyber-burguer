from telnetlib import LOGOUT
from django.shortcuts import render
from django.views.generic import TemplateView
from Api.serializers import ProdutoSerializer,ClienteSerializer,EnderecoSerializer,CarSerializer
from core.models import Produto,Cliente,Endereco,Car
from rest_framework import viewsets
#-------------------------------------------------------------------------------
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#-------------------------------------------------------------------------------
# Create your views here.




class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ClienteViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
   
    permission_classes = [IsAuthenticated]
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
class CardViewSet(viewsets.ModelViewSet):
    pass

#Autenticação---------------------------------------------------------------------
class LoginViewSet(APIView):
    pass
class CadastroViewSet(APIView):
    pass
# -------------------------------------------------------------------------------- 
