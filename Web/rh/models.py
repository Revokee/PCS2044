from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    SEX_STRINGS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=SEX_STRINGS)
    endereco = models.CharField(max_length=200)
    telefone = models.BigIntegerField()
    cpf = models.BigIntegerField()
 
    def __unicode__(self):
        return self.nome  

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=200)
    nivel = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.nome_cargo


class Contrato(models.Model):
    data_contratacao = models.DateTimeField(blank=False)
    turno = models.CharField(max_length=200)
    nome_contratante = models.CharField(max_length=200)
    observacoes = models.CharField(max_length=600)
    STATUS_CONTRATO_TIPO  = (
        ('VALIDO_OK', 'Contrato Valido'),
        ('ENCERRADO', 'Contrato Encerrado'),
    )
    status_contrato = models.CharField(max_length=9, choices=STATUS_CONTRATO_TIPO)
    data_demissao = models.DateTimeField(blank=True, null=True)
    motivo_demissao = models.CharField(blank=True, max_length=600)
    cargo = models.ForeignKey(Cargo)
    funcionario = models.OneToOneField(Funcionario, blank=True)
 
    def __unicode__(self):
        return self.funcionario.__unicode__() + " " + str(self.data_contratacao)


class Historico_Pagamentos(models.Model):
    data_mes_ano = models.DateTimeField(blank=False)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    funcionario = models.ForeignKey(Funcionario)
    
    def __unicode__(self):
        return self.funcionario.__unicode__()

class Ferias(models.Model):
    ano = models.BigIntegerField()
    data_inicio_ferias = models.DateTimeField(blank=False)
    numero_dias = models.BigIntegerField()
    funcionario = models.ForeignKey(Funcionario)

    def __unicode__(self):
        return self.funcionario.__unicode__()

class Licencas(models.Model):
    data_inicio_licenca = models.DateTimeField(blank=False)
    numero_dias = models.BigIntegerField()
    motivo = models.CharField(max_length=200)
    remunerado = models.BooleanField()
    funcionario = models.ForeignKey(Funcionario)
    
    def __unicode__(self):
        return self.funcionario.__unicode__()


"""class Historico_Profissao(models.Model):
    data_inicio_cargo = models.DateTimeField(blank=False)
    cargo = models.ForeignKey(Cargo)
    funcionario = models.ForeignKey(Funcionario)

    def __unicode__(self):
        return self.funcionario.__unicode__() + " " + str(self.data_inicio_cargo)
"""

