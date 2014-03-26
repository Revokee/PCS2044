from django.utils import simplejson
from django.http import HttpResponse
from pedido.models import *

def pedidos(request):
	response_data = Order.objects.values()
	return HttpResponse(simplejson.dumps(response_data), mimetype='application/json')