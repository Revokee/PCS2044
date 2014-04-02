# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contrato'
        db.create_table(u'rh_contrato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_contratacao', self.gf('django.db.models.fields.DateTimeField')()),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nome_contratante', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('status_contrato', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('data_demissao', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('motivo_demissao', self.gf('django.db.models.fields.CharField')(max_length=600, blank=True)),
            ('cargo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rh.Cargo'])),
            ('funcionario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['rh.Funcionario'], unique=True, blank=True)),
        ))
        db.send_create_signal(u'rh', ['Contrato'])

        # Adding model 'Ferias'
        db.create_table(u'rh_ferias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ano', self.gf('django.db.models.fields.BigIntegerField')()),
            ('data_inicio_ferias', self.gf('django.db.models.fields.DateTimeField')()),
            ('numero_dias', self.gf('django.db.models.fields.BigIntegerField')()),
            ('funcionario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rh.Funcionario'])),
        ))
        db.send_create_signal(u'rh', ['Ferias'])

        # Adding model 'Licencas'
        db.create_table(u'rh_licencas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_inicio_licenca', self.gf('django.db.models.fields.DateTimeField')()),
            ('numero_dias', self.gf('django.db.models.fields.BigIntegerField')()),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('remunerado', self.gf('django.db.models.fields.BooleanField')()),
            ('funcionario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rh.Funcionario'])),
        ))
        db.send_create_signal(u'rh', ['Licencas'])

        # Adding model 'Historico_Pagamentos'
        db.create_table(u'rh_historico_pagamentos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_mes_ano', self.gf('django.db.models.fields.DateTimeField')()),
            ('valor_pago', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('funcionario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rh.Funcionario'])),
        ))
        db.send_create_signal(u'rh', ['Historico_Pagamentos'])

        # Adding model 'Cargo'
        db.create_table(u'rh_cargo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_cargo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('salario', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'rh', ['Cargo'])

        # Adding model 'Funcionario'
        db.create_table(u'rh_funcionario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefone', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'rh', ['Funcionario'])


    def backwards(self, orm):
        # Deleting model 'Contrato'
        db.delete_table(u'rh_contrato')

        # Deleting model 'Ferias'
        db.delete_table(u'rh_ferias')

        # Deleting model 'Licencas'
        db.delete_table(u'rh_licencas')

        # Deleting model 'Historico_Pagamentos'
        db.delete_table(u'rh_historico_pagamentos')

        # Deleting model 'Cargo'
        db.delete_table(u'rh_cargo')

        # Deleting model 'Funcionario'
        db.delete_table(u'rh_funcionario')


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