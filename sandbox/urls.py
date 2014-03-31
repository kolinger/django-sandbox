from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'articles.views.default'),
                       url(r'^detail/([a-z0-9\-]+)$', 'articles.views.detail'),
                       url(r'^pages$', 'pages.views.default'),
                       url(r'^page/([a-z0-9\-]+)$', 'pages.views.detail'),
)
