from django import forms
from django.forms import ModelForm
from funcionario.models import *

class CreateFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ('pizzaria_id', 'name')

	def __init__(self, *args, **kwargs):
		super(CreateFuncionarioForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Nome do Entregador'
		self.fields['pizzaria_id'].label = 'ID da Pizzaria'

class EditFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ('latitude','longitude')