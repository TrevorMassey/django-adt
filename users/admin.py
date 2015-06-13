from django.contrib import admin
from django.utils.translation import ugettext as _

from users.models import User, Rank
from users.forms import UserChangeForm, UserCreationForm

from django.contrib.auth.admin import UserAdmin

class AddictionUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('display_name', 'username', 'slug', 'email', 'rank',)
    ordering = ('display_name', )

    fieldsets = (
        (None, {'fields': ('display_name', 'username', 'slug', 'email', 'password', 'rank', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('display_name', 'email', 'password1', 'password2'),
        }),
    )

class RankAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(User, AddictionUserAdmin)
admin.site.register(Rank, RankAdmin)
