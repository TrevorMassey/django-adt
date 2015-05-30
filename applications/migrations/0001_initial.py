# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0003_auto_20150527_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateTimeField()),
                ('timezone', models.IntegerField()),
                ('longitude', models.DecimalField(max_digits=11, decimal_places=7)),
                ('latitude', models.DecimalField(max_digits=11, decimal_places=7)),
                ('character_name', models.CharField(max_length=255)),
                ('character_class', models.CharField(max_length=255)),
                ('character_level', models.IntegerField()),
                ('technical_expertise', models.CharField(max_length=30)),
                ('technical_skills', models.TextField()),
                ('playtime', models.IntegerField()),
                ('player_type', models.CharField(max_length=30)),
                ('game_detailed_history', models.TextField()),
                ('why_join', models.TextField()),
                ('game_officer_history', models.TextField()),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'question', editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField()),
                ('chapter', models.ForeignKey(to='games.Chapter')),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='applicationanswer',
            name='question',
            field=models.OneToOneField(to='applications.ApplicationQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='answers',
            field=models.ManyToManyField(to='applications.ApplicationQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
