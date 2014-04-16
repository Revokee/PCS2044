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

	def clustering(self, lats, longs):
		raio = 3
		qtEnd = len(lats)
		i = 0
		distancias = []
		distanciasPorEnd = []
		print qtEnd
		while i < qtEnd:
			j = 0
			distancias = []
			while j < qtEnd-1:
				if i != j:
					distancias.insert(j,self.calculaDistancia(lats[i],lats[j+1],longs[i],longs[j+1]))
				else:
					distancias.insert(j,0)
				j=j+1
			distanciasPorEnd.append(distancias)
			i=i+1
		return distanciasPorEnd
    	# Multiplica-se o arco pelo raio da terra em km para obter a distancia nesta unidade de medida
	

	
