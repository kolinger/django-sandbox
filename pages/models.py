from django import forms
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from core import admin as extended_admin


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name"]


class PageForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data["name"]
        if Page.objects.filter(slug=slugify(data)).exclude(pk=self.instance.id).exists():
            raise forms.ValidationError("This name is already used")
        return data


class PageAdmin(extended_admin.ModelAdmin):
    fields = ("name", "content")
    list_display = ("name", "slug")
    form = PageForm


admin.site.register(Page, PageAdmin)