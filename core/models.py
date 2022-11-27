from platform import release
from django.db import models
from stdimage import StdImageField

from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
...
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save, post_save, m2m_changed
#user = settings.AUTH_USER_MODEL
class Base(models.Model):
    created_at = models.DateTimeField('created_at',auto_now_add=True)
    updated_at = models.DateTimeField('updated_at',auto_now=True)
    ativo = models.BooleanField('Ativo',default=True)
    class Meta:
        abstract=True      
        
class Produto(Base):
    produto_id = models.AutoField('produto_id', primary_key=True, auto_created=True)
    nome = models.CharField('Nome', max_length=100, null = False, blank = False)
    codigo_do_produto = models.IntegerField('Codigo de produto', null = False, blank = False)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9, null = False, blank = False)
    estoque = models.IntegerField("estoque", null = False, blank = False)
    foto = StdImageField('foto', upload_to='fotos/%Y/%m/', null = True, blank = True)
    descricao = models.TextField('Descrição', null=True,blank=True)

    def get_absolute_url(self):
        return f"/produto/{self.produto_id}/"

class Usuario(Base):
    usuario = models.OneToOneField( User , on_delete=models.CASCADE, unique=True)
    name = models.CharField( 'name', max_length=100, null=True)
    #email = models.CharField( 'email', max_length=100)
    telefone = models.CharField('telefone', max_length=20, null = True)
    foto = StdImageField('foto', upload_to='path/to/img', null=True)
    comentario = models.TextField('Comentario', null=True)
    rua = models.CharField("rua", max_length=50, null=True)
    numero = models.CharField("numero", max_length=50, null=True)
    cep =  models.CharField("cep", max_length=50, null=True)
    def __unicode__(self):
        return "{}".format(self.usuario, self.name, self.telefone, self.comentario, self.rua, self.numero, self.cep)

          
class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)  
    
class Cart(Base):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    produto = models.ManyToManyField(Produto, blank = True)
    total = models.DecimalField(default= 0.00,max_digits=65, decimal_places=2)
    subtotal = models.DecimalField(default= 0.00 ,decimal_places=2, max_digits=5)
    quantidade = models.PositiveIntegerField(default=1, null=True, blank=True)
    objects = CartManager()

   
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
  #print(action)
  if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
    #print(instance.products.all())
    #print(instance.total)
    products = instance.produto.all()
    total = 0 
    for product in products: 
      total += product.preco 
    if instance.subtotal != total:
      instance.subtotal = total
      instance.save()
    #print(total) 
    instance.subtotal = total
    instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender = Cart.produto.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
  instance.total = instance.subtotal + 10 # considere o 10 como uma taxa de entrega

pre_save.connect(pre_save_cart_receiver, sender = Cart)
    
    

class Order(models.Model):
    """A model that contains data for an item in an order."""
    carrinho = models.ForeignKey(
        Cart,
        related_name='order',
        on_delete=models.CASCADE
    )
    total = models.DecimalField(default = 0.00, max_digits=5, decimal_places = 2)
    status = (
        ('Ad',"Andamento"),
        ('EV',"enviado"),
        ('Fi',"Finalizado"),
        ('En',"Entregue"),
        ('Cn',"Cancelado")
    ) 
    observacao = models.TextField('Observação', null=True,blank=True)
    status_pedido = models.CharField(max_length=2, choices=status, blank=True, null=True)    
    
    def __unicode__(self):
        return "{} - {} - {} - {} - {}".format(self.carrinho , self.total, self.observacao, self.status_pedido)
    
    