from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Entrada(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_audit = models.DateTimeField(auto_now_add=True)
    data_entrada = models.DateTimeField(blank=False)
    origem = models.CharField(max_length=200)
    descricao = models.TextField()
    responsavel = models.ForeignKey(User)

    def __unicode__(self):
        return self.origem

class Saida(models.Model):
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	data_audit = models.DateTimeField(auto_now_add=True)
	data_saida = models.DateTimeField(blank=False)
	destino = models.CharField(max_length=200)
	descricao = models.TextField()
	responsavel = models.ForeignKey(User)

	def __unicode__(self):
		return self.destino    

class SaldoMes(models.Model):
	mes = models.DateField(auto_now_add=False, unique=True)
	saldo = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return str(self.mes)