from django import forms
from django.forms import ModelForm
from rh.models import *

class CreateFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ('nome', 'idade', 'sexo', 'cargo', 'telefone')

	def __init__(self, *args, **kwargs):
		super(CreateFuncionarioForm, self).__init__(*args, **kwargs)
		self.fields['nome'].label = 'Nome do Entregador'
		self.fields['idade'].label = 'Idade'
		self.fields['sexo'].label = 'Sexo'
		self.fields['cargo'].label = 'Entregador'
		self.fields['telefone'].label = 'Entregador'

class EditFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ('latitude','longitude')
