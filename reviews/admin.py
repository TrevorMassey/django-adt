from django.contrib import admin
from reviews.models import Review, Vote


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'description',)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'vote',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Vote, VoteAdmin)
