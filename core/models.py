from platform import release
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# User = settings.AUTH_USER_MODEL
class Base(models.Model):
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class Produto(Base):
    id = models.AutoField("Produto_id", primary_key=True, auto_created=True)
    nome = models.CharField("Nome", max_length=100, null=False, blank=False)
    codigo_do_produto = models.IntegerField(
        "Codigo de produto", null=False, blank=False
    )
    preco = models.DecimalField(
        "Preço", decimal_places=2, max_digits=9, null=False, blank=False
    )
    estoque = models.IntegerField("Quantidade em Estoque", null=False, blank=False)
    foto = models.ImageField("foto", blank=True, upload_to="fotos/%Y/%m/", null=True)
    descricao = models.TextField("Descrição", null=True, blank=True)

    def __str__(self):
        return self.nome


# 1 hamburgue #2 bebida


class Dados(Base):
    teleRegex = RegexValidator(regex=r"^\([1-9]{2}\) 9[7-9]{1}[0-9]{3}\-[0-9]{4}$")
    phone = models.CharField("phone", max_length=30, primary_key=True)
    foto = models.ImageField("foto", upload_to="path/to/img", blank=True)
    comentario = models.TextField("Comentario", null=True, blank=True)
    rua = models.CharField("rua", max_length=50)
    numero = models.CharField("numero", max_length=50)
    cep = models.CharField("cep", max_length=50)

    def __str__(self):
        return "dados"


class User(AbstractUser):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-Mail", max_length=100)
    password = models.CharField("Senha", max_length=50)
    # dados_cliente =  models.ForeignObject(Dados,  related_name='User',on_delete=models.CASCADE,null=True,blank=True)


"""User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
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
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)"""


class Cart(Base):
    cliente = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="Cart",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class CartItem(Base):
    cart = models.ForeignKey(
        Cart, related_name="CartItem", on_delete=models.CASCADE, null=True, blank=True
    )
    produto = models.ForeignKey(
        Produto, related_name="CartItem", on_delete=models.CASCADE
    )
    quantidade = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __unicode__(self):
        return "%s: %s" % (self.produto.nome, self.quantidade)


class Order(Base):
    status = (
        ("Ad", "Andamento"),
        ("EV", "enviado"),
        ("Fi", "Finalizado"),
        ("En", "Entregue"),
        ("Cn", "Cancelado"),
    )
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="Order",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    observacao = models.TextField("Observação", null=True, blank=True)
    status_pedido = models.CharField(
        max_length=2, choices=status, blank=True, null=True
    )
    total = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)


class OrderItem(models.Model):
    """A model that contains data for an item in an order."""

    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    produto = models.ForeignKey(
        Produto, related_name="order_items", on_delete=models.CASCADE
    )
    quantidade = models.PositiveIntegerField(null=True, blank=True)
    total = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "%s: %s" % (self.produto.nome, self.quantidade)


"""def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    print(action)
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        print(instance.total)
        produto = instance.produto.all()
        total = 0 
        for p in produto: 
            total += p.preco 
            if instance.subtotal != total:
                instance.subtotal = total
                instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender = OrderItem.produto.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal + 5 # considere o 10 como uma taxa de entrega

    pre_save.connect(pre_save_cart_receiver, sender = OrderItem)
 
"""


"""class Car(Base):
    
    id = models.AutoField('cart_id', primary_key=True, auto_created=True)
    produtos = models.ManyToManyField(Produto, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    cliente = models.OneToOneField(Cliente,related_name='Cars', on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(default = 0.00, max_digits=5, decimal_places = 2)
    subtotal = models.DecimalField(default = 0.00, max_digits=5, decimal_places = 2)
    observacao = models.TextField('Observação', null=True,blank=True)
    objects = CartManager()
    def get_produtos(self):
        return ",".join([str(p) for p in self.produtos.all()])
    def __str__(self):
        return str(self.id)
    """
