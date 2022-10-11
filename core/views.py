
from django.views.generic import TemplateView

from core.serializers import ProdutoSerializer
from core.models import Produto,Cliente,Endereco,Pedido
from rest_framework import viewsets

class IndexView(TemplateView):
    template_name = 'index.html'
    

class MenuView(TemplateView):
    template_name = 'menu/food.html'
    
class AboutView(TemplateView):
    template_name = 'menu/about.html'
    
class BookView(TemplateView):
    template_name = 'menu/book.html'



# ViewSets define the view behavior.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
