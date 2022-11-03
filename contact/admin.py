from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "read", "created", "updated"]
    list_filter = ["read", "created", "updated"]
    search_fields = ["name", "subject", "message"]