from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pedido.forms import *
from pedido.models import *
from pygeocoder import Geocoder

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from unidecode import unidecode
import lxml.html

# Funcao para cadastrar um pedido
@csrf_exempt 
def create_pedido(request):
	if request.method=='GET':
		create_order_form = CreateOrderForm()
		return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))
	else:
		create_order_form = CreateOrderForm(request.POST)
		if create_order_form.is_valid():
			new_pedido = create_order_form.save(commit=False)
			address = ''+create_order_form.cleaned_data['rua']+','+str(create_order_form.cleaned_data['numero'])+','+create_order_form.cleaned_data['cidade']
			results = Geocoder.geocode(address)
			latitude, longitude = results[0].coordinates
			new_pedido.latitude = latitude
			new_pedido.longitude = longitude
			new_pedido.save()
			messages.success(request, 'Pedido Cadastrado com sucesso')
			return HttpResponseRedirect('/pedidos/')
		messages.info(request, 'Formulario Nao OK')
		return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))

#Funcao para remover um pedido
def delete_pedido(request, pedido_id):
	pedido = Order.objects.get(pk=pedido_id)
	pedido.delete()
	messages.warning(request,'Pedido Deletado com sucesso')
	return HttpResponseRedirect('/pedidos/')


#Funcao para listar todos os pedidos
def index(request):
	orders = Order.objects.values()
	return render_to_response('pedidos.html', locals(), context_instance=RequestContext(request))

class OrderManager():

	def __init__(self, home):
		self.home = unidecode(unicode(home, 'utf-8'))

	def _get_webdriver(self):
		driver = None
		i = 0
		while driver == None:
			if i == 0:
				try:
					driver = webdriver.Chrome()
					print "Chrome webdriver selected"
				except Exception:
					pass
			elif i == 1:
				try:
					driver = webdriver.Firefox()
					print "Firefox webdriver selected"
				except Exception:
					pass
			elif i == 2:
				driver = webdriver.Ie()
				print "Internet Explorer webdriver selected"
			i += 1
		return driver

	def bestRoute(self, addresses):
		for i in range(len(addresses)):
			addresses[i] = unidecode(unicode(addresses[i], 'utf-8'))
		download = True
		if download:	
			display = Display(visible=0, size=(800, 600))
			display.start()
			driver = self._get_webdriver()
			url = "http://www.routexl.com/?q="
			url += self.home + "$"
			for address in addresses:
				url += address + "$"
			url = url[:-1]
			print url
			driver.get(url)
			try:
				WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'performance')))
			except Exception:
				print "failed (timeout)"
				return None
			page = driver.page_source.encode('utf-8')
		else:
			page = open("testpage").read()
		#print page
		html = lxml.html.fromstring(page)
		route = {"time": None, "distance": None, "addresses": []}
		for element in html.xpath('//div[@id="route-canvas"]//b'):
			#print element.text
			route["addresses"].append(element.text)
		params = route["addresses"][-1][route["addresses"][-1].rfind("time"):].split()
		route["time"] = params[1] + " " + params[2]
		route["distance"] = params[4] + " " + params[5]
		del route["addresses"][0]
		del route["addresses"][-1]
		del route["addresses"][-1]
		if download:
			driver.quit()
			display.stop()
		return route
