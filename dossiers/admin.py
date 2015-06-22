from django.contrib import admin
from dossiers.models import UserRole, DossierRole, Guild, Dossier, Heading, Note, Issue


class GuildAdmin(admin.ModelAdmin):
    list_display = ('title',)


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'duration',)


class DossierRoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'duration',)


class DossierAdmin(admin.ModelAdmin):
    list_display = ('subject',)


class HeadingAdmin(admin.ModelAdmin):
    list_display = ('title',)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('heading',)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('created',)

admin.site.register(Guild, GuildAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(DossierRole, DossierRoleAdmin)
admin.site.register(Dossier, DossierAdmin)
admin.site.register(Heading, HeadingAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Issue, IssueAdmin)

