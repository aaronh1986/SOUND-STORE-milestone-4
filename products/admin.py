from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('-sku',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)