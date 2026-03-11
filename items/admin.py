from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "price",
        "category",
        "status",
        "owner",
        "created_at"
    )

    list_filter = (
        "category",
        "status"
    )

    search_fields = (
        "title",
        "description"
    )