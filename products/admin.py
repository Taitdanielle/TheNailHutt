from django.contrib import admin
from .models import Product, Category, Services

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'image_url'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'service',
    )    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)
