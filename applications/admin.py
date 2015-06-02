from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from applications.models import Application, ApplicationAnswer, ApplicationQuestion


class ApplicationAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ['state']


admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationAnswer)
admin.site.register(ApplicationQuestion)


