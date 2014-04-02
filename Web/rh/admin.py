from django.contrib import admin
from pizza5.rh.models import Funcionario
from pizza5.rh.models import Contrato
from pizza5.rh.models import Cargo
from pizza5.rh.models import Ferias
from pizza5.rh.models import Licencas
from pizza5.rh.models import Historico_Pagamentos
"from pizza5.rh.models import Historico_Profissao"

admin.site.register(Funcionario)
admin.site.register(Contrato)
admin.site.register(Cargo)
admin.site.register(Ferias)
admin.site.register(Licencas)
admin.site.register(Historico_Pagamentos)
"admin.site.register(Historico_Profissao)"
# Register your models here.
