from django.contrib import admin
from financeiro.models import Entrada, Saida, SaldoMes, FormaPagamento

admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(SaldoMes)
admin.site.register(FormaPagamento)