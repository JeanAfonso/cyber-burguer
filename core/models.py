from django.db import models
from stdimage import StdImageField
from phonenumber_field.modelfields import PhoneNumberField
#from django.contrib.auth.base_user import BaseUserManager
#from django.contrib.auth.models import AbstractUser

class Base(models.Model):
    created_at = models.DateTimeField('created_at',auto_now_add=True)
    updated_at = models.DateTimeField('updated_at',auto_now=True)
    ativo = models.BooleanField('Ativo',default=True)
    class Meta:
        abstract=True
        
        
class Produto(Base):
    nome = models.CharField('Nome', max_length=100, null = False, blank = False)
    codigo_do_produto = models.IntegerField('Codigo de produto', null = False, blank = False)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9, null = False, blank = False)
    estoque = models.IntegerField("Quantidade em Estoque", null = False, blank = False)
    foto = StdImageField('foto', upload_to='fotos/%Y/%m/', null = False, blank = False)
    descricao = models.TextField('Descrição', null=True,blank=True)

    def __str__(self):
        return self.nome


class Endereco(Base):
    rua = models.CharField("rua", max_length=50)
    numero = models.CharField("numero", max_length=50)
    cep =  models.CharField("cep", max_length=50)    
    def __str__(self):
        return self.rua
      
class Cliente(Base):
    nome = models.CharField('Nome', max_length=100, null = False, blank = False)
    sobrenome = models.CharField('sobrenome', max_length=100, null = False, blank = False)
    email = models.EmailField('Email', max_length=100, null = False, blank = False)
    telefone = PhoneNumberField('Telefone', unique = True, null = False, blank = False, primary_key=True)
    endereco = models.ForeignKey("Endereco", related_name='Cliente', on_delete=models.CASCADE, null = False, blank = False)
    foto = StdImageField('foto', upload_to='path/to/img', blank=True)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return str(self.telefone)

"""
class CartManager(models.manager):
    def new_or_get(self, request):
        cart_id = request.session.get("ID_Car", None)
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.Cliente.is_authenticate and cart_obj.user is None:
                cart_obj.Cliente = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user = request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticate:
                user_obj = user
        return self.model.objects.create(user = user_obj)    
"""    
class Car(Base):
    id = models.AutoField('ID_Car', primary_key=True, auto_created=True)
    produtos = models.ManyToManyField("Produto", blank=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(default = 0.00, max_digits=5, decimal_places = 2)
    observacao = models.TextField('Observação', null=True,blank=True)
    #objects = CartManager()
    def get_produtos(self):
        return ",".join([str(p) for p in self.produtos.all()])
    def __str__(self):
        return str(self.id)

class Pedido(Base):
    status = (
        ('Ad',"Andamento"),
        ('EV',"enviado"),
        ('Fi',"Finalizado"),
        ('En',"Entregue"),
        ('Cn',"Cancelado")
    ) 
    status_pedido = models.CharField(max_length=2, choices=status, blank='Ad', null='Ad')
 
"""

class Cliente(models.Model):
    nome= models.CharField(_("nome"), max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
"""