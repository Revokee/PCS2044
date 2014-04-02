# RESTful api for pizza5/estoque
from tastypie import fields
from tastypie.authorization import Authorization
from pizza5.api import *
from pizza5.estoque.models import *

class IngredienteResource(BaseModelResource):		
		
		class Meta:
				queryset = Ingrediente.objects.all()
				resource_name = 'ingrediente'
				allowed_methods = ['get','post']
				authorization = Authorization()