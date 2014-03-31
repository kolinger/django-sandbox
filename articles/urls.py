from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'articles.views.default'),
                       url(r'^detail/([a-z0-9\-]+)$', 'articles.views.detail'),
)
