from django.contrib import admin
from django.db import models
from django import forms


class ModelAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": forms.Textarea(attrs={"class": "ckeditor"})}}

    class Media:
        js = ("/static/ckeditor/ckeditor.js",)
        css = {"all": ("/static/admin.css",)}
