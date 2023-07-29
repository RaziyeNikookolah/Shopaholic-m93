from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Address)


class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False
    extra: int = 0


class AddressInline(admin.StackedInline):
    model = models.Address
    extra = 1


@admin.register(models.Account)
class CustomAccountAdmin(UserAdmin):
    model = models.Account
    list_display = ('phone_number', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (_("Personal info"), {
         "fields": ("first_name", "last_name", "email", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        # (_("Important dates"), {"fields": (,#"last_login", "date_joined"
        #                                    )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number",  # , "password1", "password2", 'role'
                           ),
            },
        ),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)
    # date_hierarchy = 'date_joined'

    inlines = (ProfileInline, AddressInline)
