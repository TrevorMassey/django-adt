# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AdminLog(models.Model):
    record = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    timestamp = models.IntegerField()
    type = models.IntegerField()
    action = models.CharField(max_length=100)
    info = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'admin_log'


class GameHistory(models.Model):
    record = models.IntegerField(primary_key=True)
    user = models.IntegerField()
    starttime = models.IntegerField()
    stoptime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game_history'


class WebsiteLogin(models.Model):
    record = models.IntegerField(primary_key=True)
    timestamp = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    account = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website_login'
