import re
from django.views.generic import TemplateView
from requests import request
from core.models import Produto,User,Cart


#-------------------------------------------------------------------------------
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#-------------------------------------------------------------------------------

class IndexView(TemplateView):
    template_name = 'index.html'
    

class MenuView(TemplateView):
    template_name = 'sessao_2/menu/food.html'
    
class AboutView(TemplateView):
    template_name = 'sessao_2/menu/about.html'
    
class BookView(TemplateView):
    template_name = 'sessao_2/menu/book.html'
    

    
    
class PedidoView(TemplateView):
    template_name = 'sessao_2\pedido\pedido.html'


def ProdutoListView(request):
    
    produto = Produto.objects.get(id =1)
    print(produto)
    context = {
        'id' : produto.id,
        'nome': produto.nome, 
        'codigo_do_produto': produto.codigo_do_produto,
        'descricao':  produto.descricao,
        'preco': produto.preco,
        'foto': produto.foto,
    }
    return render(request, 'sessao_2/menu/food.html', context=context)

"""    queryset = Produto.objects.all()
    template_name = 'sessao_2/menu/food.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProdutoListView).get_context_data(**kwargs)
        cart_obj, new_obj = Car.objects.new_or_get(self.request)
        
        context["cart"] = cart_obj
        return context
    """
    
    
def cart_home(request):
    cart_obj, new_obj  = Cart.objects.new_or_get(request)
    return render(request, "sessao_2/carrinho/carrinho.html", {})


"""
def cart_update(request):
    product_id = 2
    # Pega o produto com id 5
    product_obj = Produto.objects.get(id=product_id)
    # Cria ou pega a instância já existente do carrinho
    cart_obj, new_obj = Car.objects.new_or_get(request)
    if product_obj in cart_obj.produtos.all():
        cart_obj.produtos.remove(product_obj) # cart_obj.products.remove(product_id)
        print("entrou")
        # E o produto se adiciona a instância do campo M2M 
        cart_obj.produtos.add(product_obj) # cart_obj.products.add(product_id)
    
    # retorna redirect(product_obj.get_absolute_url())
    return redirect(cart_home)"""