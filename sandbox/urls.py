from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf.urls.static import static

from articles import urls as articles_urls
from pages import urls as pages_urls
from sandbox import settings


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include(articles_urls)),
                       url(r'', include(pages_urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
