from django.contrib import admin
from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "category", "owner", "status", "created_at"]
    list_filter = ["category", "status", "created_at"]
    search_fields = ["title", "description"]