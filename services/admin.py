from django.contrib import admin
from .models import Services, ServicesDetail
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'description',
        'price',
        'is_a_service',
        'image',
        'image_url'
    )

class ServicesDetailAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Services, ServicesDetailAdmin)