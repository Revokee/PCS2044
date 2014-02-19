from django import forms
from django.forms import ModelForm
from orderGrouping.models import *

class CreatePedidoForm(forms.ModelForm)
	class Meta:
		model = Order
		fields = ('pizzas_number', 'latitude', 'longitude')