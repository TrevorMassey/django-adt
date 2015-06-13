from django.contrib import admin
from accounting.models import DonateAmount, DonateCost, DonateGoal


class DonateAmountAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount',)


class DonateCostAdmin(admin.ModelAdmin):
    list_display = ('service', 'amount',)

class DonateGoalAdmin(admin.ModelAdmin):
    list_display = ('amount', 'created', 'end', 'description',)

admin.site.register(DonateAmount, DonateAmountAdmin)
admin.site.register(DonateCost, DonateCostAdmin)
admin.site.register(DonateGoal, DonateGoalAdmin)
