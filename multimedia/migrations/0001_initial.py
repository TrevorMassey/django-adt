# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('type', models.CharField(max_length=15, choices=[(b'internal', b'internal source'), (b'external', b'external source')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('involved', models.ManyToManyField(related_name='quotes', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('poster', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
