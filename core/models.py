from django.db import models
from stdimage import StdImageField
from phonenumber_field.modelfields import PhoneNumberField

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
    comentario = models.TextField('Comentario', null=True,blank=True)

    def __str__(self):
        return self.nome

class Carrinho():
    id = models.CharField("ID_Carrinho", max_length=120, blank=True)
    produtos = models.ManyToManyField("Produto", related_name='pedidos')
    
    
    
    
class Pedido(Base):
    id = models.AutoField('ID_Pedido',primary_key=True,auto_created=True)
    status = (
        ('Ad',"Andamento"),
        ('EV',"enviado"),
        ('Fi',"Finalizado"),
        ('En',"Entregue"),
        ('Cn',"Cancelado")
    )
    status_pedido = models.CharField(max_length=2, choices=status, blank='Ad', null='Ad')
    observacao = models.TextField('Observação',null=True,blank=True)
    produtos = models.ManyToManyField("Produto",related_name='pedidos')
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    total = models.DecimalField("Total",default = 0.00, max_digits=2, decimal_places = 2)
    
    def get_produtos(self):
        return ",".join([str(p) for p in self.produtos.all()])
    def __str__(self):
        return str(self.id)

"""

class Cliente(models.Model):
    nome= models.CharField(_("nome"), max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
"""