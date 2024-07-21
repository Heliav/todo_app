from django.contrib import admin
import django.contrib.auth.admin
from todo_app.users.models import User


class CustomUserAdmin(django.contrib.auth.admin.UserAdmin):
    model = User
    fieldsets = django.contrib.auth.admin.UserAdmin.fieldsets + (
        (None, {'fields': 'date_of_birth'}),
    )
    add_fieldsets = django.contrib.auth.admin.UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'date_of_birth')}),
    )

    admin.site.register(User, django.contrib.auth.admin.UserAdmin)
