"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    # Add what is listed on admin page
    ordering = ['id']
    list_display = ['email', 'name']
    # Sections displayed based on custom user model
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    # Support for creating users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # For custom CSS styling
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


# Assigns the custom UserAdmin class for the model manager
admin.site.register(models.User, UserAdmin)
admin.site.register(models.MSISD)
