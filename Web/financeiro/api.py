# RESTful api for pizza5/financeiro 
from tastypie import fields
from tastypie.authorization import Authorization
from pizza5.api import *
from pizza5.financeiro.models import *
from django.contrib.auth.models import User

# *******************
# ** Utils Methods **
# *******************

# find user by username and create tastypie resource url with user's id
def get_user_url_by_username(username):
		responsavel = User.objects.get(username = str(username))
		return '/api/rest/user/' + str(responsavel.id) + "/"

# find formapagamento by username and create tastypie resource url with formapagamento's id
def get_forma_pagamento_url_by_codigo(codigo):
		forma_pagamento = FormaPagamento.objects.get(codigo = str(codigo))
		return '/financeiro/api/rest/forma_pagamento/' + str(forma_pagamento.id) + "/"		

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
				bundle.data['responsavel'] = get_user_url_by_username(bundle.data['responsavel'])
				bundle.data['forma_pagamento'] = get_forma_pagamento_url_by_codigo(bundle.data['forma_pagamento'])
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
				bundle.data['responsavel'] = get_user_url_by_username(str(bundle.data['responsavel']))
				# returns the created resource
				return super(SaidaResource, self).obj_create(bundle, **kwargs)						