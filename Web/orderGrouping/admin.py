from orderGrouping.models import Order
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
	list_display= ('pizzas_number', 'latitude', 'longitude')

admin.site.register(Order, OrderAdmin)