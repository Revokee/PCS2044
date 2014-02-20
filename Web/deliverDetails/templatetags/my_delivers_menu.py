from django import template
from deliverDetails.models import Deliver
register = template.Library()

@register.inclusion_tag('meus_entregadores_menu.html')
def my_delivers():
	delivers = Deliver.objects.values()
	return {'delivers':delivers}