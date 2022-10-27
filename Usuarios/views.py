"""from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Produto,User
from core.forms import ClienteForm

from django.views.generic.edit import FormView,CreateView
# Create your views here.
from django.shortcuts import render
#https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView
from django.contrib import messages

    
def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print("------------------------------------------ cadastro",form.is_valid())
        endereco = EnderecoForm(request.POST)
        if form.is_valid():
            
            form.instance.endereco = endereco
            validacao = form.save(commit = False)
            messages.success(request, 'cadastro salvo com sucesso.')
            print('cadastro feito com sucesso')
            validacao.save()
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ClienteForm()
    context = {
        'form': form,
        
    }
    return render(request, 'sessao_3/cad/cadastro.html', context)
class UsuarioView(TemplateView):
    template_name = 'sessao_3/user/perfil.html'"""
    