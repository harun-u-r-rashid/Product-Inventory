from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ['name', 'slug']

admin.site.register(models.Product, ProductAdmin)

