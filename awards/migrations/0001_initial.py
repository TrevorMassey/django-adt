# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awards.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('level_limit', models.IntegerField()),
                ('order', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AwardCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AwardImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('image', models.ImageField(upload_to=awards.models.award_image_path)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AwardRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('award', models.ForeignKey(to='awards.Award')),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
    ]
