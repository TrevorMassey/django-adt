from django.contrib import admin
from dkp.models import Location, Entity, Item, Section, Bonus, Resource, ResourceContrib, Event, EventAttendance, \
    EventEntity, EventItem, Transaction


class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'game',)

class EntityAdmin(admin.ModelAdmin):
    list_display = ('title', 'location',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'entity',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter',)

class BonusAdmin(admin.ModelAdmin):
    list_display = ('user', 'dkp',)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'dkp', 'section',)

class ResourceContribAdmin(admin.ModelAdmin):
    list_display = ('amount', 'user', 'resource',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location',)

class EventAttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'user',)

class EventEntityAdmin(admin.ModelAdmin):
    list_display = ('event', 'entity',)

class EventItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'credit', 'debit',)

admin.site.register(Location, LocationAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceContrib, ResourceContribAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventAttendance, EventAttendanceAdmin)
admin.site.register(EventEntity, EventEntityAdmin)
admin.site.register(EventItem, EventItemAdmin)
admin.site.register(Transaction, TransactionAdmin)
