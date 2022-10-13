from django import forms
#from core.models import Produto,Cliente,Endereco,Pedido
from django import forms

from core.models import Car, Cliente, Produto, Endereco


class PedidoForm(forms.Form):
    observacao = forms.CharField(label = 'Nome')
    total = forms.DecimalField(label = "Total")

class EnderecoForm(forms.Form):
    rua = forms.CharField(label ='rua')
    numero = forms.CharField(label ='numero')
    cep = forms.CharField(label ='cep')
    
    
class ClienteForm(forms.Form):
    nome = forms.CharField(label ='Nome')
    sobrenome = forms.CharField(label ='sobrenome')
    email = forms.CharField(label ='email')
    telefone = forms.CharField(label ='telefone')

