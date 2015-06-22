# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_slugs(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slugs)
    ]
