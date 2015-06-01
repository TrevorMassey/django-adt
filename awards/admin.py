from django.contrib import admin
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage, AwardType


class AwardAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AwardCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AwardRecipientAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'award', 'created', 'reason',)

class AwardImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)

admin.site.register(Award, AwardAdmin)
admin.site.register(AwardCategory, AwardCategoryAdmin)
admin.site.register(AwardRecipient, AwardRecipientAdmin)
admin.site.register(AwardImage, AwardImageAdmin)
admin.site.register(AwardType)
