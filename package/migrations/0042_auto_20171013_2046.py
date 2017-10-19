# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 20:46
from __future__ import unicode_literals

from django.db import migrations


def migrate_false_to_none(apps, schema_editor):
    #  We can't import the Person model directly as it may be a newer
    #  version than this migration expects. We use the historical version.

    TeamMembership = apps.get_model('package', 'TeamMembership')
    for tm in TeamMembership.objects.all():
        tm.role_confirmed = None
        tm.save()


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0041_auto_20171013_2035'),
    ]

    operations = [
        migrations.RunPython(migrate_false_to_none),
    ]