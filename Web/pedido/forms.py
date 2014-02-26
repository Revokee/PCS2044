from django import forms
from django.forms import ModelForm
from pedido.models import *
from django.utils.translation import gettext as _

class CreateOrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('rua','numero','cidade')

	def __init__(self, *args, **kwargs):
		super(CreateOrderForm, self).__init__(*args, **kwargs)
		self.fields['numero'].label = 'Numero'