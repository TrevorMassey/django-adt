# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20150605_0219'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multimedia', '0002_auto_20150609_0001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='screenshot',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='screenshot',
            name='chapter',
            field=models.ForeignKey(default=1, to='games.Chapter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 0, 20, 37, 728509, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='involved',
            field=models.ManyToManyField(related_name='screenshots', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='poster',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
