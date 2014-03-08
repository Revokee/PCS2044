from django.db import models

#Model que representa o fluxo de caixa
class Caixa(models.Model):
	valor = models.FloatField()
	#Se deve ser somado ou descontado
	tipo = models.CharField(max_length=128)
	criado_em = models.DateTimeField()
	descontado_em = models.DateTimeField()
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	pizzaria = models.ForeignKey('cliente.Pizzaria')
	#Quem cadastrou o debito
	funcionario = models.ForeignKey('rh.Funcionario')
