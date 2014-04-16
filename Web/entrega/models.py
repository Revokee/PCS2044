from django.db import models
from rh.models import Funcionario

# Create your models here.
class Entrega(models.Model):
	# ID do entregador
	entregador = models.ForeignKey('entrega.Entregador')

class Entregador(Funcionario):
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	disponivel = models.BooleanField(default=False)
	atualizado_em = models.DateTimeField(auto_now_add=True)

class Geoposicao(models.Model):
	entregador = models.ForeignKey('entrega.Entregador')
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	criado_em = models.DateTimeField(auto_now_add=True)