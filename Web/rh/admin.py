from django.contrib import admin
from rh.models import Funcionario
from rh.models import Contrato
from rh.models import Cargo
from rh.models import Ferias
from rh.models import Licencas
from rh.models import Historico_Pagamentos
"from rh.models import Historico_Profissao"

admin.site.register(Funcionario)
admin.site.register(Contrato)
admin.site.register(Cargo)
admin.site.register(Ferias)
admin.site.register(Licencas)
admin.site.register(Historico_Pagamentos)
"admin.site.register(Historico_Profissao)"
# Register your models here.
