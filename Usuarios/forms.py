

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e
    

"""
from django import forms
from core.models import Usuario



from django.contrib.auth.models import User 


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'Username'}))
    class Meta:
        model = User
        fields = ('username',)


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = (
            'name'
            'telefone',
            'rua',
            'numero',
            'cep',
      
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
"""