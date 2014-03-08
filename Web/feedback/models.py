from django.db import models

# Create your models here.
class Feedback(models.Model):
	comentario = models.CharField(max_length=2048)
	endereco = models.ForeignKey('cliente.Usuario')
	pizzaria = models.ForeignKey('cliente.Pizzaria')