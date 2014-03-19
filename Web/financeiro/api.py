# RESTful api for pizza5/financeiro 
from tastypie import fields
from tastypie.authorization import Authorization
from PCS2044.api import *
from financeiro.models import *
from django.contrib.auth.models import User


# api for the Entrada functionality
class EntradaResource(BaseModelResource):
		responsavel = fields.ForeignKey(UserResource, 'responsavel', full=True)

		class Meta:
				queryset = Entrada.objects.all()
				resource_name = 'entrada'
				allowed_methods = ['get','post']
				authorization = Authorization()

		def obj_create(self, bundle, **kwargs):
				# find user by username
				responsavel_username = str(bundle.data['responsavel'])
				responsavel = User.objects.get(username = responsavel_username)
				# create tastypie resource url with user's id
				bundle.data['responsavel'] = '/api/rest/user/' + str(responsavel.id) + "/" 
				# returns the created resource
				return super(EntradaResource, self).obj_create(bundle, **kwargs)		

		""" date formating > check
		def dehydrate(self, bundle):
				bundle.data['data_entrada'] = bundle.data['data_entrada'].__format__("%d/%m/%y %H:%M:%S")
				bundle.data['data_audit'] = bundle.data['data_audit'].__format__("%d/%m/%y %H:%M:%S")
				return bundle
		"""

# api for the Saida functionality
class SaidaResource(BaseModelResource):
		responsavel = fields.ForeignKey(UserResource, 'responsavel', full=True)

		class Meta:
				queryset = Saida.objects.all()
				resource_name = 'saida'
				allowed_methods = ['get','post']
				authorization = Authorization() #TODO: real authorization and authentication

		def obj_create(self, bundle, **kwargs):
				# find user by username
				responsavel_username = str(bundle.data['responsavel'])
				responsavel = User.objects.get(username = responsavel_username)
				# create tastypie resource url with user's id
				bundle.data['responsavel'] = '/api/rest/user/' + str(responsavel.id) + "/" 
				# returns the created resource
				return super(SaidaResource, self).obj_create(bundle, **kwargs)	