from django.contrib import admin
from .models import Division, Product, Category


class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'division',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'brand',
        'name',
        'size',
        'amount',
        'color',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Division, DivisionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
