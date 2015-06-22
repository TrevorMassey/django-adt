# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20150605_0219'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dossiers', '0002_auto_20150531_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'subject', editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('subject_rel', models.OneToOneField(related_name='dossier', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DossierRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('duration', models.PositiveIntegerField()),
                ('dossier', models.ForeignKey(to='dossiers.Dossier')),
                ('game', models.ForeignKey(related_name='dossiers_dossierrole_game', to='games.Game')),
                ('guild', models.ForeignKey(related_name='dossiers_dossierrole_guild', to='dossiers.Guild')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='dossier_notes', to=settings.AUTH_USER_MODEL)),
                ('heading', models.ForeignKey(to='dossiers.Heading')),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('duration', models.PositiveIntegerField()),
                ('game', models.ForeignKey(related_name='dossiers_userrole_game', to='games.Game')),
                ('guild', models.ForeignKey(related_name='dossiers_userrole_guild', to='dossiers.Guild')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='role',
            name='application',
        ),
        migrations.RemoveField(
            model_name='role',
            name='game',
        ),
        migrations.RemoveField(
            model_name='role',
            name='guild',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
