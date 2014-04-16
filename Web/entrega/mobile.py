from django.db import models

from django.http.response import HttpResponse
import json

def login(request):
	a = ["teste" for i in range(5)]
	respjson = json.dumps(a)
	return HttpResponse(respjson)

def push_location(request):
	entregador = {"id": None, "latitude": None, "longitude": None}
	entregador["id"] = request.GET.get('id', None)
	entregador["latitude"] = request.GET.get('lat', None)
	entregador["longitude"] = request.GET.get('long', None)
	respjson = json.dumps(entregador)
	return HttpResponse(respjson)


# Create your models here.
