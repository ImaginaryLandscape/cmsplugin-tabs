# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TabHeaderPlugin'
        db.create_table('cmsplugin_tabheaderplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tab_count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cmsplugin_tabs', ['TabHeaderPlugin'])

        # Adding model 'TabTitle'
        db.create_table('cmsplugin_tabs_tabtitle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('tab_header', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_tabs.TabHeaderPlugin'])),
        ))
        db.send_create_signal('cmsplugin_tabs', ['TabTitle'])

    def backwards(self, orm):
        # Deleting model 'TabHeaderPlugin'
        db.delete_table('cmsplugin_tabheaderplugin')

        # Deleting model 'TabTitle'
        db.delete_table('cmsplugin_tabs_tabtitle')

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_tabs.tabheaderplugin': {
            'Meta': {'object_name': 'TabHeaderPlugin', 'db_table': "'cmsplugin_tabheaderplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'tab_count': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'cmsplugin_tabs.tabtitle': {
            'Meta': {'object_name': 'TabTitle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tab_header': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_tabs.TabHeaderPlugin']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['cmsplugin_tabs']