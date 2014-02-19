from django.db import models

# Model que representa um pedido de um cliente
class Order(models.Model):
	#def __unicode__(self):
	#	return self.pizzas_number
	pizzas_number = models.IntegerField(default=1)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
    #pizzaria = models.ForeignKey('users.Pizzaria')
    #costumer = models.ForeignKey('users.Costumers')
    ##############################################################
    ##############################################################
    #Se os models precisarem de metodos adicionais, adicionar aqui
    #Ex.: def far_far_away?(self):
    #		if longitude > (pizzaria.longitude+10000)
    #			return true  
    #		else
    #			return false
    #No Controller: Order.far_far_away?

#Model que representa a capacidade de uma entrega dada a pizzaria
class Capacity(models.Model):
	#def __unicode__(self):
	#	return self.delivery_capacity
	#pizzaria = models.ForeignKey('users.Pizzaria')
	delivery_capacity = models.IntegerField(default=1) 

#Model que representa para uma pizzaria se ha entregadores disponiveis
class Availability(models.Model):
	#def __unicode__(self):
	#	return self.deliver_availables
	deliver_availables = models.IntegerField(default=0)
	#pizzaria = models.ForeignKey('users.Pizzaria')