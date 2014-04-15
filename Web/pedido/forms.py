from django import forms
from django.forms import ModelForm
from pedido.models import *
from django.utils.translation import gettext as _

class PedidoForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = ('pizza_id', 'quantidade', 'rua', 'numero', 'complemento', 'cidade')

	def __init__(self, *args, **kwargs):
		super(PedidoForm, self).__init__(*args, **kwargs)
