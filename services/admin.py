from django.contrib import admin

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
        'service',
    )

admin.site.register(Services, ServicesAdmin)
admin.site.register(Services, ServicesDetailAdmin)