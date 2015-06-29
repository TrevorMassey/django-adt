# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0012_auto_20150613_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dkp', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'bonus',
                'verbose_name_plural': 'bonuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('dkp', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'entity',
                'verbose_name_plural': 'entities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('started', models.DateTimeField(null=True, blank=True)),
                ('stopped', models.DateTimeField(null=True, blank=True)),
                ('scheduled', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('event_leader', models.ForeignKey(related_name='events_ran', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('stopped', models.DateTimeField(null=True, blank=True)),
                ('standby', models.BooleanField(default=False)),
                ('event', models.ForeignKey(related_name='attendees', to='dkp.Event')),
                ('user', models.ForeignKey(related_name='event_attandance', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-started',),
                'verbose_name': 'eventattendance',
                'verbose_name_plural': 'eventattendance',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entity', models.ForeignKey(related_name='kills', to='dkp.Entity')),
                ('event', models.ForeignKey(related_name='entities', to='dkp.Event')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'evententity',
                'verbose_name_plural': 'evententities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dkp', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attendee', models.ForeignKey(related_name='items', to='dkp.EventAttendance')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'eventitem',
                'verbose_name_plural': 'eventitems',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('boss', models.ForeignKey(related_name='items', to='dkp.Entity')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('dkp', models.IntegerField(default=1)),
                ('game', models.ForeignKey(related_name='+', to='games.Game')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('dkp', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResourceContrib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(related_name='contributions', to='dkp.Resource')),
                ('user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'resourcecontribution',
                'verbose_name_plural': 'resourcecontributions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(related_name='dkp_section', to='games.Chapter')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='resource',
            name='section',
            field=models.ForeignKey(related_name='resources', to='dkp.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventitem',
            name='item',
            field=models.ForeignKey(related_name='awarded_items', to='dkp.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(related_name='events', to='dkp.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='section',
            field=models.ForeignKey(related_name='events', to='dkp.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entity',
            name='location',
            field=models.ForeignKey(related_name='bosses', to='dkp.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bonus',
            name='section',
            field=models.ForeignKey(related_name='bonus_dkp', to='dkp.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bonus',
            name='user',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
