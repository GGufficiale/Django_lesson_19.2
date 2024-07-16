from django.contrib import admin
from catalog.models import Product, Category

# """Вывод продуктов"""
# admin.site.register(Product)

"""Вывод списка продуктов"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
