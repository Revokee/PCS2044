# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MedidaIngrediente'
        db.create_table(u'estoque_medidaingrediente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Ingrediente'])),
            ('medida', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'estoque', ['MedidaIngrediente'])

        # Adding model 'Inventario'
        db.create_table(u'estoque_inventario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Ingrediente'], unique=True)),
            ('quantidade', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=0)),
        ))
        db.send_create_signal(u'estoque', ['Inventario'])

        # Adding model 'Ingrediente'
        db.create_table(u'estoque_ingrediente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descricao', self.gf('django.db.models.fields.CharField')(default='-', max_length=300)),
        ))
        db.send_create_signal(u'estoque', ['Ingrediente'])

        # Adding model 'ListaCompras'
        db.create_table(u'estoque_listacompras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Ingrediente'])),
            ('medidaIngrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.MedidaIngrediente'])),
            ('quantidade', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=0)),
        ))
        db.send_create_signal(u'estoque', ['ListaCompras'])

        # Adding model 'HistoricoCompras'
        db.create_table(u'estoque_historicocompras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listaCompras', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.ListaCompras'])),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'estoque', ['HistoricoCompras'])


    def backwards(self, orm):
        # Deleting model 'MedidaIngrediente'
        db.delete_table(u'estoque_medidaingrediente')

        # Deleting model 'Inventario'
        db.delete_table(u'estoque_inventario')

        # Deleting model 'Ingrediente'
        db.delete_table(u'estoque_ingrediente')

        # Deleting model 'ListaCompras'
        db.delete_table(u'estoque_listacompras')

        # Deleting model 'HistoricoCompras'
        db.delete_table(u'estoque_historicocompras')


    models = {
        u'estoque.historicocompras': {
            'Meta': {'object_name': 'HistoricoCompras'},
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listaCompras': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['estoque.ListaCompras']"})
        },
        u'estoque.ingrediente': {
            'Meta': {'object_name': 'Ingrediente'},
            'descricao': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'estoque.inventario': {
            'Meta': {'object_name': 'Inventario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['estoque.Ingrediente']", 'unique': 'True'}),
            'quantidade': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '0'})
        },
        u'estoque.listacompras': {
            'Meta': {'object_name': 'ListaCompras'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['estoque.Ingrediente']"}),
            'medidaIngrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['estoque.MedidaIngrediente']"}),
            'quantidade': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '0'})
        },
        u'estoque.medidaingrediente': {
            'Meta': {'object_name': 'MedidaIngrediente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['estoque.Ingrediente']"}),
            'medida': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['estoque']