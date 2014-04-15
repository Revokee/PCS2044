#-*- coding: utf-8 -*-
from django.db import models

from entrega.models import Entrega

##################################
######################	AVISO AOS NAVEGANTES: ISSO É UM STUB!
##################################

# Create your models here.
class Pedido(models.Model):
	pizza_id = models.IntegerField(default=1)
	quantidade = models.IntegerField(default=1)
	#Adicionar para verificar se o pedido foi entregue
	entregue = models.BooleanField()
        pago = models.BooleanField()
	#Para quem deve ser entregue
	#cliente = models.ForeignKey('cliente.Usuario')
	#Pizzaria dona da entrega
	#pizzaria = models.ForeignKey('cliente.Pizzaria')
	rua = models.CharField(max_length=1024)
        numero = models.IntegerField(default=1)
        cidade =  models.CharField(max_length=1024)
        complemento = models.CharField(max_length=1024, null=True)
        latitude = models.FloatField(default=0)
        longitude = models.FloatField(default=0)
        #pizzaria_id = models.IntegerField(default=1)
	entrega = models.ForeignKey('entrega.Entrega', null=True)
