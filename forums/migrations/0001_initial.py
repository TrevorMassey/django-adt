# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import django.db.models.deletion
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('type', models.CharField(max_length=15, choices=[(b'category', b'category'), (b'forum', b'forum'), (b'link', b'link')])),
                ('link_url', models.URLField(null=True, blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('topics', models.PositiveIntegerField(default=0)),
                ('posts', models.PositiveIntegerField(default=0)),
                ('last_post_on', models.DateTimeField(null=True, blank=True)),
                ('last_thread_title', models.CharField(max_length=255, null=True, blank=True)),
                ('last_thread_slug', models.CharField(max_length=255, null=True, blank=True)),
                ('last_poster_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_poster_avatar', models.CharField(max_length=255, null=True, blank=True)),
                ('last_poster_rank_color', models.CharField(max_length=255, null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('last_poster', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True)),
                ('css_class', models.CharField(max_length=255, null=True, blank=True)),
                ('forums', models.ManyToManyField(to='forums.Forum')),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('edits', models.PositiveIntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.DateTimeField(null=True, blank=True)),
                ('deleted_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('forum', models.ForeignKey(to='forums.Forum')),
                ('last_editor', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-created',),
                'permissions': (('soft_delete_post', 'Can soft delete post'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'title', blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('replies', models.PositiveIntegerField(default=0, db_index=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('is_announcement', models.BooleanField(default=False, db_index=True)),
                ('is_pinned', models.BooleanField(default=False, db_index=True)),
                ('is_poll', models.BooleanField(default=False)),
                ('is_locked', models.BooleanField(default=False)),
                ('last_post_on', models.DateTimeField(db_index=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.DateTimeField(null=True, blank=True)),
                ('deleted_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('first_post', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='forums.Post', null=True)),
                ('forum', models.ForeignKey(to='forums.Forum')),
                ('label', models.ForeignKey(blank=True, to='forums.Label', null=True)),
                ('last_post', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='forums.Post', null=True)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'permissions': (('soft_delete_topic', 'Can soft delete topic'),),
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='topic',
            index_together=set([('forum', 'last_post_on'), ('forum', 'replies'), ('forum', 'id')]),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='forums.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forum',
            name='last_thread',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='forums.Topic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forum',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='forums.Forum', null=True),
            preserve_default=True,
        ),
    ]
