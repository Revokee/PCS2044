from django import template
from deliverDetails.models import Deliver
register = template.Library()

@register.inclusion_tag('meus_entregadores_menu.html')
def my_delivers():
	delivers = Deliver.objects.values()
	return {'delivers':delivers}

@register.inclusion_tag('meus_entregadores_local.html')
def my_delivers_local():
	delivers = Deliver.objects.values()
	return {'delivers':delivers}