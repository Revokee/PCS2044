from django.db import models

# Create your models here.
class Entrega(models.Model):
	# ID do entregador
	entregador = models.CharField(max_length=1024)
