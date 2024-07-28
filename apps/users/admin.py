from django.contrib import admin
import django.contrib.auth.admin
from apps.users.models import User, Notification

admin.site.register(Notification)


class CustomUserAdmin(django.contrib.auth.admin.UserAdmin):
    model = User
    fieldsets = django.contrib.auth.admin.UserAdmin.fieldsets + (
        (None, {"fields": "date_of_birth"}),
    )
    add_fieldsets = django.contrib.auth.admin.UserAdmin.add_fieldsets + (
        (None, {"fields": ("email", "date_of_birth")}),
    )

    admin.site.register(User, django.contrib.auth.admin.UserAdmin)
