from django.db import models

#Model que representa um entregador
class Deliver(models.Model):
	pizzaria_id = models.IntegerField(default=0)
	name = models.CharField(max_length=1024)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	available = models.BooleanField()
	updated_at = models.DateTimeField(auto_now_add=True)