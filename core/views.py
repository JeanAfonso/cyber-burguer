from django.views.generic import TemplateView
from core.serializers import ProdutoSerializer,ClienteSerializer,EnderecoSerializer,CarSerializer
from core.models import Produto,Cliente,Endereco,Car
from rest_framework import viewsets
#-------------------------------------------------------------------------------
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#-------------------------------------------------------------------------------

class IndexView(TemplateView):
    template_name = 'index.html'
    

class MenuView(TemplateView):
    template_name = 'menu/food.html'
    
class AboutView(TemplateView):
    template_name = 'menu/about.html'
    
class BookView(TemplateView):
    template_name = 'menu/book.html'
    
class CadastroView(TemplateView):
    template_name = 'cadastro/cadastro.html'
    
    
#Autenticação---------------------------------------------------------------------
class LoginViewSet(APIView):
    pass
class CadastroViewSet(APIView):
    pass
# ViewSets define the view behavior.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class loginview(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)