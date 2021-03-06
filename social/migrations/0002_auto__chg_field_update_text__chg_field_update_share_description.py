# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Update.text'
        db.alter_column(u'social_update', 'text', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Update.share_description'
        db.alter_column(u'social_update', 'share_description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Update.text'
        db.alter_column(u'social_update', 'text', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True))

        # Changing field 'Update.share_description'
        db.alter_column(u'social_update', 'share_description', self.gf('django.db.models.fields.CharField')(max_length=600, null=True))

    models = {
        u'social.apitoken': {
            'Meta': {'object_name': 'ApiToken'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'social.brokenfeed': {
            'Meta': {'unique_together': "(('type', 'origin_id'),)", 'object_name': 'BrokenFeed'},
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'check_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'social.feed': {
            'Meta': {'unique_together': "(('type', 'origin_id'),)", 'object_name': 'Feed'},
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'update_error_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'social.update': {
            'Meta': {'ordering': "['-created_time']", 'unique_together': "(('feed', 'origin_id'),)", 'object_name': 'Update'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '350', 'null': 'True'}),
            'share_caption': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True'}),
            'share_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'share_link': ('django.db.models.fields.URLField', [], {'max_length': '350', 'null': 'True'}),
            'share_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'sub_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['social']