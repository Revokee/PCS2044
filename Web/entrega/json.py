from django.utils import simplejson
from django.http import HttpResponse
from entrega.models import *

def entregas(request):
	response_data = Entrega.objects.values()
	return HttpResponse(simplejson.dumps(response_data), mimetype='application/json')
