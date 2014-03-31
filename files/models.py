from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.template.defaultfilters import slugify
from os import path
from django.db import models

from core import admin as extended_admin


class File(models.Model):
    id = models.AutoField(primary_key=True)
    upload_date = models.DateTimeField(verbose_name="Upload date", default=datetime.now)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="files")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.file.name
        super(File, self).save(*args, **kwargs)


class FileAdmin(extended_admin.ModelAdmin):
    exclude = ("upload_date", "name")
    list_display = ("name", "upload_date")


admin.site.register(File, FileAdmin)
