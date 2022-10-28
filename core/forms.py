from django.forms import ModelForm

from core.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


"""class ClienteForm(ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'sobrenome', 'email','phone','foto','rua', 'numero', 'cep']
        
        
    def clean(self):
        super(ClienteForm, self).clean() 
        if 'nome' in self.cleaned_data and 'email' in self.cleaned_data:
            nome = self.cleaned_data['nome']
            email_one = self.cleaned_data['email']
            valor = User.objects.get_or_create(email=email_one)

            if valor == False:
                raise ValidationError('email já exite!')
            else:
                print('esta ok')
                return self.cleaned_data"""
