# RESTful api for pizza5/financeiro 
from tastypie import fields
from tastypie.authorization import Authorization
from pizza5.api import *
from pizza5.estoque.models import *
from django.contrib.auth.models import User


class IngredienteResource(BaseModelResource):		
		class Meta:
				queryset = Ingrediente.objects.all()
				resource_name = 'ingrediente'
				allowed_methods = ['get']
				authorization = Authorization()

		""" date formating > check
		def dehydrate(self, bundle):
				bundle.data['data_entrada'] = bundle.data['data_entrada'].__format__("%d/%m/%y %H:%M:%S")
				bundle.data['data_audit'] = bundle.data['data_audit'].__format__("%d/%m/%y %H:%M:%S")
				return bundle
		"""
