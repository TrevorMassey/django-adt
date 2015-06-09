from django.contrib import admin
from multimedia.models import Quote, Screenshot


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)

class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)

