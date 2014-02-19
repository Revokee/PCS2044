from django import forms
from orderGrouping.forms import *
from orderGrouping.models import *

# Funcao para cadastrar um pedido
def create_order(request)
	if request.method=='GET':
		create_order_form = CreateOrderForm()
	else:
		create_order_form = CreateOrderForm(request.POST)
		if create_order_form.is_valid():
			pizzas_number = create_order_form.cleaned_data['orders']
			latitude = create_order_form.cleaned_data['latitude']
			longitude = create_order_form.cleaned_data['longitude']
		order = Order(pizzas_number = pizzas_number, longitude=longitude, latitude=latitude)
		order.save()
		render_to_response('pedidos.html', )		