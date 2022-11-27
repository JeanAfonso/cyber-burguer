from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Produto,Usuario


from django.views.generic.edit import FormView,CreateView
# Create your views here.
from django.shortcuts import render
#https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
#https://docs.djangoproject.com/en/4.1/topics/auth/default/
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from core.models import Usuario
from Usuarios.forms import UsuarioForm
from django.shortcuts import redirect
from django.shortcuts import render 
from django.contrib.auth import logout


class UsuarioCreate(CreateView):
    template_name = "sessao_3\cad\cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
  
        grupo = get_object_or_404(Group, name="cliente")
        
        
        url = super().form_valid(form) 
        Usuario.objects.create(usuario=self.object)    
        self.object.groups.add(grupo)
        self.object.save()

       

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context

    
class PerfilUpdate(UpdateView):
    template_name = r"sessao_3\cad\atualizar.html"
    model = Usuario
    fields = ['foto','name','telefone','rua','numero','cep']
    success_url =  reverse_lazy('index')
    
    def get_object(self,queryset = None):
        self.object = get_object_or_404(Usuario)
        return self.object
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "dados usuario"
        context['botao'] = "Cadastrar"

        return context
    
    

def UsuarioView(request):
   
    usuario = Usuario.objects.get()

 
    context= {
                    'foto': usuario.foto,
                    'name': usuario.name,
                    'telefone': usuario.telefone,
                    'rua': usuario.rua,
                    'cep': usuario.cep }
    return render(request, 'sessao_3/user/perfil.html',context)
   


"""
def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    def cadastroView(request):
        if request.method == 'POST':
        username = request.POST.get('username', None)
        nome = request.POST.get('nome', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        rua = request.POST.get('rua', None)
        numero = request.POST.get('numero', None)
        cep = request.POST.get('cep', None)

        novoUsuario = User.objects.create_user(username=username, email=email, password=password)
        print(novoUsuario, '------------------------------------------------------------------------------------------------------')
     
        novoUsuario.save()
        novoUsuario.usuario.telefone = telefone
        novoUsuario.usuario.nome = nome
        novoUsuario.usuario.rua = rua
        novoUsuario.usuario.numero = numero
        novoUsuario.usuario.cep = cep
        print('deu certo',novoUsuario)
       
    return render(request, 'sessao_3/cad/cadastro.html')

"""