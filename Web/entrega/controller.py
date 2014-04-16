#-*- coding: utf-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from unidecode import unidecode
import lxml.html
#Clustering
import math # math needed for sqrt

class EntregaController:
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
			#addresses[i] = unidecode(unicode(addresses[i], 'utf-8'))
			addresses[i] = unidecode(addresses[i])
		download = True
		if download:	
			display = Display(visible=0, size=(800,600))
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
				WebDriverWait(driver, 360).until(EC.presence_of_element_located((By.ID, 'performance')))
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

	def calculaDistancia(self, lat1,lat2, long1,long2):
		i = 0
		# Conversao de latitude e longitude de coordenadas esféricas para radianos
		degrees_to_radians = math.pi/180.0
		# phi = 90 - latitude
		phi1 = (90.0 - lat1)*degrees_to_radians
		phi2 = (90.0 - lat2)*degrees_to_radians
		# theta = longitude
		theta1 = long1*degrees_to_radians
		theta2 = long2*degrees_to_radians
		cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1-theta2)+math.cos(phi1)*math.cos(phi2))
		arc = math.acos(cos)		
		return arc*6373

	def clustering(self, pedidos):
		lats = [pedido["latitude"] for pedido in pedidos]
		longs = [pedido["longitude"] for pedido in pedidos]
		#lasf = pedidos[0]["latitude"]
		#print lasf
		raio = 3
		qtEnd = len(lats)
		#print qtEnd
		i = 0
		clusters = []
		distancias = []
		distanciasPorEnd = []
		#print qtEnd
		#Calcula distancias uma a uma entre cada pedido
		

		for pedido in pedidos:
			j = 0
			distancias = []
			while j < len(pedidos):
				distancias.insert(j,self.calculaDistancia(lats[i],lats[j],longs[i],longs[j]))
				j=j+1
			distanciasPorEnd.append(distancias)
			i=i+1
		
		#for distancias in distanciasPorEnd:
			#print distancias

		pedidosRestantes = []
		todosPedidos =[]
		
		for pedido in pedidos:
			todosPedidos.append(pedido)

		for pedido in pedidos:
			pedidosRestantes.append(pedido)

		#print 'pedidoRestante'
		#for pedidoRestante in pedidosRestantes:
			#print pedidoRestante
		#print 'pedidoRestante'

		allClusters = []
		cluster = []
		cluster.append(todosPedidos[0])
		pedidosRestantes.remove(todosPedidos[0])
		#for cl in cluster:
		#	print cl
		for distanciaPorEnd in distanciasPorEnd:
			#dentro de uma lista da (lista de listas)
			j = 0
			for distancia in distanciaPorEnd:
				#print 'raio '+str(raio) + ' distancia '+str(distancia)+' todosPedidos['+str(j)+']'+ str(todosPedidos[j])
				#print ''
				if(distancia < raio and distancia != 0 and (todosPedidos[j] in pedidosRestantes)):
					#print 'entrou'
					cluster.append(todosPedidos[j])
					pedidosRestantes.remove(todosPedidos[j])
				j += 1
			if cluster:
				allClusters.append(cluster)
				cluster = []
		i = 0		
		#for cls in allClusters:
			#print ''
			#msg = 'Cluster ' + str(i)
			#print msg
			#print cls

		return allClusters



