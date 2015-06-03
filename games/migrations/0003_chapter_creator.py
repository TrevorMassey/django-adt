# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0002_chapter_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='creator',
            field=models.ForeignKey(related_name='+', default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
