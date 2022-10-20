
#from core.models import Produto,Cliente,Endereco,Pedido
from django.forms import ModelForm

from core.models import  Cliente,Endereco


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'cep']

    
    
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'foto','comentario']
