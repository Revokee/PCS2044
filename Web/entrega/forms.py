from django import forms
from django.forms import ModelForm
from entrega.models import *
from django.utils.translation import gettext as _

class EntregaForm(forms.ModelForm):
	class Meta:
		model = Entrega
		fields = ('entregador',)

	def __init__(self, *args, **kwargs):
		super(EntregaForm, self).__init__(*args, **kwargs)
