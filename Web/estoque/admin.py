from django.contrib import admin
from estoque.models import Ingrediente, MedidaIngrediente, Inventario, ListaCompras, HistoricoCompras

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(Inventario)
admin.site.register(MedidaIngrediente)
admin.site.register(ListaCompras)
admin.site.register(HistoricoCompras)
