# RESTful api for pizza5/financeiro 
from tastypie import fields
from tastypie.authorization import Authorization
from PCS2044.api import *
from financeiro.models import *
from django.contrib.auth.models import User

# *******************
# ** Utils Methods **
# *******************

def get_value_by_key(object, key):
		try:
				return object[key]
		except Exception, e:
				return None


USER_API_URL_PATTERN = '/api/rest/user/%s/'
FORMA_PAGAMENTO_API_URL_PATTERN = '/financeiro/api/rest/forma_pagamento/%s/'

# find user by username and create tastypie resource url with user's id
def get_user_url_by_username(username):
		responsavel = User.objects.get(username = str(username))
		return USER_API_URL_PATTERN % str(responsavel.id)

# find formapagamento by username and create tastypie resource url with formapagamento's id
def get_forma_pagamento_url_by_codigo(codigo):
		forma_pagamento = FormaPagamento.objects.get(codigo = str(codigo))
		return FORMA_PAGAMENTO_API_URL_PATTERN % str(forma_pagamento.id)

def adequate_resource(resource):
		responsavel = get_value_by_key(resource, 'responsavel')
		if(responsavel is not None):
				resource['responsavel'] = get_user_url_by_username(responsavel)
		
		forma_pagamento = get_value_by_key(resource, 'forma_pagamento')
		if(forma_pagamento is not None):
				resource['forma_pagamento'] = get_forma_pagamento_url_by_codigo(forma_pagamento)					

# *****************
# ** Entrada api **
# *****************

class FormaPagamentoResource(BaseModelResource):
		class Meta:
				queryset = FormaPagamento.objects.all()
				resource_name = 'forma_pagamento'
				allowed_methods = ['get']
				authorization = Authorization()

class EntradaResource(BaseModelResource):
		responsavel = fields.ForeignKey(UserResource, 'responsavel', full=True)
		forma_pagamento = fields.ForeignKey(FormaPagamentoResource, 'forma_pagamento', full=True)

		class Meta:
				queryset = Entrada.objects.all()
				resource_name = 'entrada'
				allowed_methods = ['get','post']
				authorization = Authorization()

		def obj_create(self, bundle, **kwargs):
				adequate_resource(bundle.data)			
				print(bundle)
				# returns the created resource
				return super(EntradaResource, self).obj_create(bundle, **kwargs)		


# ****************
# ** Saida api **
# ****************

class SaidaResource(BaseModelResource):
		responsavel = fields.ForeignKey(UserResource, 'responsavel', full=True)

		class Meta:
				queryset = Saida.objects.all()
				resource_name = 'saida'
				allowed_methods = ['get','post']
				authorization = Authorization()
		
		def obj_create(self, bundle, **kwargs):
				adequate_resource(bundle.data)			
				print(bundle)
				# returns the created resource
				return super(SaidaResource, self).obj_create(bundle, **kwargs)						