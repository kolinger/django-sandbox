from django.db import models
from django.contrib import admin


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()


class PageAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Page, PageAdmin)