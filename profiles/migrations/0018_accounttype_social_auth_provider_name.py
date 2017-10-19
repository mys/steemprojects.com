# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-15 15:11
from __future__ import unicode_literals

from django.db import migrations, models


def init_default(apps, schema_editor):
    #  We can't import the Person model directly as it may be a newer
    #  version than this migration expects. We use the historical version.
    AccountType = apps.get_model('profiles', 'AccountType')

    for account_type in AccountType.objects.all():
        if account_type.name == "STEEM":
            account_type.social_auth_provider_name = "steemconnect"
        elif account_type.name == "GITHUB":
            account_type.social_auth_provider_name = "github"

        account_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_accounttype_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounttype',
            name='social_auth_provider_name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.RunPython(init_default),
    ]