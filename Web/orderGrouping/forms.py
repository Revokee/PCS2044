from django import forms
from django.forms import ModelForm
from orderGrouping.models import *
from django.utils.translation import gettext as _

class CreateOrderForm(forms.ModelForm):
	#pizzas_number
	class Meta:
		model = Order
		fields = ('pizzas_number', 'latitude', 'longitude')

	def __init__(self, *args, **kwargs):
		super(CreateOrderForm, self).__init__(*args, **kwargs)
		self.fields['pizzas_number'].label = 'Quantidade de Pizzas'