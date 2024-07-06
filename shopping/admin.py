# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/ == #

from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display	= [ "id","name", "price" ]


admin.site.register(Product,ProductAdmin)
