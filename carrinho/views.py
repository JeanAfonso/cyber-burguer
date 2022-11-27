from django.shortcuts import render
import re
from django.views.generic import TemplateView
from requests import request
from core.models import Produto,Cart

from django.shortcuts import render, redirect
#-------------------------------------------------------------------------------
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.produto.all()
    total = 0
    for product in products:
        total += product.preco
    print(total,'--------------------------------------------------------------------------------------------------------------------------------------------')
    cart_obj.total = total
    cart_obj.save()
    return render(request, "sessao_2/carrinho/carrinho.html", {})


def cart_update(request):
    product_id = 1
    # Pega o produto com id 5
    product_obj = Produto.objects.get(produto_id=product_id)
    # Cria ou pega a instância já existente do carrinho
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # E o produto se adiciona a instância do campo M2M 
    cart_obj.produto.add(product_obj) # cart_obj.products.add(product_id)
    #cart_obj.products.remove(product_obj) # cart_obj.products.remove(product_id)
    #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")
