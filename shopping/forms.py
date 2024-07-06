# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/ == #

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model	= Product
        fields	= [ "name", "price" ]

