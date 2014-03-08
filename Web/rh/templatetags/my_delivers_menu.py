from django import template
from rh.models import Funcionario
register = template.Library()

@register.inclusion_tag('meus_entregadores_menu.html')
def my_delivers():
	delivers = Funcionario.objects.values()
	return {'delivers':delivers}

@register.inclusion_tag('meus_entregadores_local.html')
def my_delivers_local():
	delivers = Funcionario.objects.values()
	return {'delivers':delivers}