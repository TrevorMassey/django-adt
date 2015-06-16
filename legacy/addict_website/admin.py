from django.contrib import admin
from legacy.addict_website.models import Users
# Register your models here.

class LegacyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'rank', 'email',)
    search_fields = ('username', )

admin.site.register(Users, LegacyUserAdmin)
