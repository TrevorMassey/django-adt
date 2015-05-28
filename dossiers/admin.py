from django.contrib import admin
from dossiers.models import Role, Guild


class GuildAdmin(admin.ModelAdmin):
    list_display = ('title',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'duration',)


admin.site.register(Guild, GuildAdmin)
admin.site.register(Role, RoleAdmin)
