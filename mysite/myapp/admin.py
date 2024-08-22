from django.contrib import admin
from .models import Products
# Register your models here.


admin.site.site_header = "SnapTrade"
admin.site.site_title = "SnapTrade Admin"
admin.site.index_title = "Manage SnapTrade"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc')
    search_fields = ('name',)



    def set_price_to_zero(self,request,queryset):
        queryset.update(price=0)

    actions = ('set_price_to_zero',)
    list_editable = ('price','desc')



admin.site.register(Products,ProductAdmin)