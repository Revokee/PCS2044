from django.db import models

# Create your models here.
class Detalhes(models.Model):
	metade1Sabor = models.CharField(max_length=256)
	metade2Sabor = models.CharField(max_length=256)
	quantidade = models.IntegerField(default=1)
	#Endereco de Entrega
	order = models.ForeignKey('pedido.Order')
	#Para quem deve ser entregue
	#cliente = models.ForeignKey('cliente.Usuario')
	#Pizzaria dona da entrega
	#pizzaria = models.ForeignKey('cliente.Pizzaria')

class Order(models.Model):
	rua = models.CharField(max_length=1024)
	numero = models.IntegerField(default=1)
	cidade =  models.CharField(max_length=1024)
	complemento = models.CharField(max_length=1024)
	#Adicionar para verificar se o pedido foi entregue
	entregue = models.BooleanField()
	pago = models.BooleanField()
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	pizzaria_id = models.IntegerField(default=1)
