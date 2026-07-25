from django.contrib import admin
from .models import Book, Branch, Inventory

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'city', 'state', 'phone')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('book', 'branch', 'quantity')