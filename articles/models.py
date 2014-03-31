from django import forms
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.utils.datetime_safe import datetime

from core import admin as extended_admin


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class CategoryForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data["name"]
        if Category.objects.filter(slug=slugify(data)).exclude(pk=self.instance.id).exists():
            raise forms.ValidationError("This name is already used")
        return data


class CategoryAdmin(extended_admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ("name", "slug")
    form = CategoryForm


admin.site.register(Category, CategoryAdmin)


#------------------------------ tag ------------------------------#


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class TagForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data["name"]
        if Tag.objects.filter(slug=slugify(data)).exclude(pk=self.instance.id).exists():
            raise forms.ValidationError("This name is already used")
        return data


class TagAdmin(extended_admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ("name", "slug")
    form = TagForm


admin.site.register(Tag, TagAdmin)


#------------------------------ article ------------------------------#


class Article(models.Model):
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(verbose_name="Create date", default=datetime.now)
    publish_date = models.DateTimeField(verbose_name="Publish date", blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class ArticleForm(forms.ModelForm):
    def clean_title(self):
        data = self.cleaned_data["title"]
        if Article.objects.filter(slug=slugify(data)).exclude(pk=self.instance.id).exists():
            raise forms.ValidationError("This name is already used")
        return data


class ArticleAdmin(extended_admin.ModelAdmin):
    exclude = ("slug", "create_date")
    list_display = ("title", "slug", "create_date", "publish_date")
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)
