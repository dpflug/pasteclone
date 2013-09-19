# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paste'
        db.create_table(u'pastebin_paste', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 9, 19, 0, 0))),
            ('accessed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 9, 19, 0, 0))),
        ))
        db.send_create_signal(u'pastebin', ['Paste'])


    def backwards(self, orm):
        # Deleting model 'Paste'
        db.delete_table(u'pastebin_paste')


    models = {
        u'pastebin.paste': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Paste'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 19, 0, 0)'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 19, 0, 0)'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['pastebin']