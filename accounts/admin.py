from django.contrib import admin
from  accounts.models import Profile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Extras",
            {
                "fields": (
                    "avatar",
                ),
            },
        ),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "country"]
    list_filter = ["country",]
    search_fields = ["user", "country"]