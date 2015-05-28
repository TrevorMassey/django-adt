from django.contrib import admin
from accounting.models import DonateAmount, DonateCost


class DonateAmountAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount',)


class DonateCostAdmin(admin.ModelAdmin):
    list_display = ('service', 'amount',)

admin.site.register(DonateAmount, DonateAmountAdmin)
admin.site.register(DonateCost, DonateCostAdmin)
