from django.db import models

# Create your models here.
class Usuario(models.Model):
	email = models.CharField(max_length=512)
	senha = models.CharField(max_length=8)
	telefone = models.CharField(max_length=16)
	nome = models.CharField(max_length=1024)
	endereco = models.OneToOneField('address.Endereco')

#Model que representa o fluxo de caixa
class Pizzaria(models.Model):
	#Se deve ser somado ou descontado
	nome = models.CharField(max_length=128)
	cnpj = models.CharField(max_length=128)
	email = models.CharField(max_length=256)
	senha = models.CharField(max_length=8)
	telefone = models.CharField(max_length=128)
	endereco = models.OneToOneField('address.Endereco')