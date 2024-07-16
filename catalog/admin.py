from django.contrib import admin
from catalog.models import Product, Category

# """Вывод продуктов"""
# admin.site.register(Product)

"""Вывод списка студентов"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'photo', )
    list_filter = ('name', 'description', 'price',)
    search_fields = ('name', 'description', 'price',)
