from django.db import models

from django.http.response import HttpResponse
import json

from datetime import datetime
from entrega.models import Entregador, Geoposicao

def _login(entregador):
	allow = False
	print entregador["id"]
	credencial = Entregador.objects.get(pk = entregador["id"])
	if credencial and credencial.password == entregador["pw"]:
		allow = True
	return allow

def _get_entregador(request):
	entregador_id = request.GET.get('id', None)
	entregador_pw = request.GET.get('p', None)
	entregador = None
	if entregador_id and entregador_pw:
		entregador = {"id": entregador_id, "pw": entregador_pw}
	return entregador
	

def login(request):
	entregador = _get_entregador()
	respjson = json.dumps(a)
	return HttpResponse(respjson)

def _push_posicao(entregador, posicao):
	entregador = Entregador.objects.get(pk = entregador["id"])
	entregador.atualizado_em = datetime.now()
	entregador.latitude = float(posicao["latitude"])
	entregador.longitude = float(posicao["longitude"])
	entregador.save()

def push_posicao(request):
	response = False
	entregador = _get_entregador(request)
	if entregador and  _login(entregador):
		latitude = request.GET.get('lat', None)
		longitude = request.GET.get('long', None)
		posicao = None
		if latitude and longitude:
			posicao = {"latitude": latitude, "longitude": longitude}
			_push_posicao(entregador, posicao)
	respjson = json.dumps(response)
	return HttpResponse(respjson)

def listar_entregas(request):
	pass

def escolher_entrega(request):
	pass

def fechar_pedido(request):
	pass

# Create your models here.
