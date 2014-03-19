# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from rh.models import *


class CreateFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ('nome', 'idade', 'sexo', 'cargo', 'telefone')

	def __init__(self, *args, **kwargs):
		super(CreateFuncionarioForm, self).__init__(*args, **kwargs)
		self.fields['nome'].label = 'Nome do Funcionário'
		self.fields['idade'].label = 'Idade'
		self.fields['sexo'].label = 'Sexo'
		self.fields['cargo'].label = 'Cargo'
		self.fields['telefone'].label = 'Telefone'

class EditFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ('latitude','longitude')
