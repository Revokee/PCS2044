from django.db import models

#Model para representar o Endereco
class Endereco(models.Model):
	rua = models.CharField(max_length=1024)
	bairro = models.CharField(max_length=1024)
	numero = models.IntegerField(default=1)
	complemento = models.CharField(max_length=64)
	cidade =  models.CharField(max_length=1024)
	estado = models.CharField(max_length=2)
	#Usado no modulo de pedidos, se alguem for fazer o crud nao precisa
	#se preocupar com estes campos
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	cep = models.CharField(max_length=45)