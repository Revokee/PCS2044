from django.db import models

#Model que define um funcionario no RH
class Funcionario(models.Model):
	nome = models.CharField(max_length=256)
	idade = models.IntegerField(default=21)
	sexo = models.CharField(max_length=32)
	cargo = models.CharField(max_length=64)
	telefone = models.CharField(max_length=16)
	#Usado para entregadores.
	latitude =  models.FloatField(default=1000)
	longitude = models.FloatField(default=1000)
	atualizado_em = models.DateTimeField(auto_now=True)
	disponivel = models.BooleanField()
	#Chaves Estrangeiras
	endereco = models.OneToOneField('address.Endereco')
	pizzaria = models.OneToOneField('cliente.Pizzaria')
	#Tive que adicionar o sufixo id para retirar um conflito
	contrato_id = models.OneToOneField('rh.Contrato')

#Model que define um contrato de um funcionario
class Contrato(models.Model):
	valorPago = models.FloatField(default=1000)
	periodo = models.CharField(max_length=256)
	carga_horaria = models.IntegerField(default=1)
	contratado_em = models.DateTimeField()
	#ID do Funcionario, veja que no momento que o contrato for feito, 
	#ja deve existir um ID do funcionario, portanto cuidado ao fazer o CRUD
	funcionario_id = models.OneToOneField('rh.Funcionario')