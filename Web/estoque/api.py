# RESTful api for pizza5/estoque
from tastypie import fields
from tastypie.authorization import Authorization
from PCS2044.api import *
from estoque.models import *

class IngredienteResource(BaseModelResource):		
		
		class Meta:
				queryset = Ingrediente.objects.all()
				resource_name = 'ingrediente'
				allowed_methods = ['get','post']
				authorization = Authorization()