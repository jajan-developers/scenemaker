# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SceneProp.always_visible'
        db.add_column(u'API_sceneprop', 'always_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Scene.next_scene'
        db.add_column(u'API_scene', 'next_scene',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='scenes', null=True, to=orm['API.Scene']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SceneProp.always_visible'
        db.delete_column(u'API_sceneprop', 'always_visible')

        # Deleting field 'Scene.next_scene'
        db.delete_column(u'API_scene', 'next_scene_id')


    models = {
        u'API.background': {
            'Meta': {'object_name': 'Background'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'API.prop': {
            'Meta': {'object_name': 'Prop'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'API.scene': {
            'Meta': {'object_name': 'Scene'},
            'background': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenes'", 'null': 'True', 'to': u"orm['API.Background']"}),
            'background_scale': ('django.db.models.fields.DecimalField', [], {'default': '1.0', 'max_digits': '8', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'next_scene': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenes'", 'null': 'True', 'to': u"orm['API.Scene']"}),
            'props': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['API.Prop']", 'through': u"orm['API.SceneProp']", 'symmetrical': 'False'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'API.sceneprop': {
            'Meta': {'object_name': 'SceneProp'},
            'always_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'movable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prop_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['API.Prop']"}),
            'rotation': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '8', 'decimal_places': '2'}),
            'scale': ('django.db.models.fields.DecimalField', [], {'default': '1.0', 'max_digits': '8', 'decimal_places': '2'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['API.Scene']"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['API']