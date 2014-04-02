from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, default="-")

    def __unicode__(self):
        return self.nome + " - " + self.marca


class MedidaIngrediente(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, blank=False)
    medida = models.CharField(max_length=30)

    def __unicode__(self):
        return self.medida

class Inventario(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, unique=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=0) 

    def __unicode__(self):
        return self.ingrediente.__unicode__() + " - " + str(self.quantidade)

class ListaCompras(models.Model):
    ingrediente = models.ForeignKey(Ingrediente)
    medidaIngrediente = models.ForeignKey(MedidaIngrediente)
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)

    def __unicode__(self):
        return self.ingrediente.__unicode__() + " - " + str(self.quantidade)

class HistoricoCompras(models.Model):
    listaCompras = models.ForeignKey(ListaCompras)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.listaCompras.__unicode__()