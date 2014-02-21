from django import forms
from django.forms import ModelForm
from deliverDetails.models import *

class CreateDeliverForm(forms.ModelForm):
	class Meta:
		model = Deliver
		fields = ('pizzaria_id', 'name')

	def __init__(self, *args, **kwargs):
		super(CreateDeliverForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Nome do Entregador'
		self.fields['pizzaria_id'].label = 'ID da Pizzaria'

class EditDeliverForm(forms.ModelForm):
	class Meta:
		model = Deliver
		fields = ('latitude','longitude')