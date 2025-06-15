from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)

# from django.contrib import admin
# from unfold.admin import ModelAdmin
# from your_app.models import Product
# from your_app.sites import new_admin_site

# @admin.register(Product, site=new_admin_site)
# class ProductAdmin(ModelAdmin):
#     pass
