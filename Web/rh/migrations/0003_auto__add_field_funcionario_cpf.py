# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Funcionario.cpf'
        db.add_column(u'rh_funcionario', 'cpf',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Funcionario.cpf'
        db.delete_column(u'rh_funcionario', 'cpf')


    models = {
        u'rh.cargo': {
            'Meta': {'object_name': 'Cargo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nome_cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salario': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'rh.contrato': {
            'Meta': {'object_name': 'Contrato'},
            'cargo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rh.Cargo']"}),
            'data_contratacao': ('django.db.models.fields.DateTimeField', [], {}),
            'data_demissao': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'funcionario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rh.Funcionario']", 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo_demissao': ('django.db.models.fields.CharField', [], {'max_length': '600', 'blank': 'True'}),
            'nome_contratante': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'status_contrato': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'rh.ferias': {
            'Meta': {'object_name': 'Ferias'},
            'ano': ('django.db.models.fields.BigIntegerField', [], {}),
            'data_inicio_ferias': ('django.db.models.fields.DateTimeField', [], {}),
            'funcionario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rh.Funcionario']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_dias': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'rh.funcionario': {
            'Meta': {'object_name': 'Funcionario'},
            'cpf': ('django.db.models.fields.BigIntegerField', [], {}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefone': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'rh.historico_pagamentos': {
            'Meta': {'object_name': 'Historico_Pagamentos'},
            'data_mes_ano': ('django.db.models.fields.DateTimeField', [], {}),
            'funcionario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rh.Funcionario']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor_pago': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'rh.licencas': {
            'Meta': {'object_name': 'Licencas'},
            'data_inicio_licenca': ('django.db.models.fields.DateTimeField', [], {}),
            'funcionario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rh.Funcionario']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numero_dias': ('django.db.models.fields.BigIntegerField', [], {}),
            'remunerado': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['rh']