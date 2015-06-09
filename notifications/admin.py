from django.contrib import admin
from notifications.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('type',)

admin.site.register(Notification, NotificationAdmin)
