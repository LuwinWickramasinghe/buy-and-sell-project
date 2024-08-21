from django.contrib import admin
from .models import Products
# Register your models here.


admin.site.site_header = "SnapTrade"
admin.site.site_title = "SnapTrade Admin"
admin.site.index_title = "Manage SnapTrade"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc')
    search_fields = ('name',)
    


admin.site.register(Products,ProductAdmin)