from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^pages$', 'pages.views.default'),
                       url(r'^page/([a-z0-9\-]+)$', 'pages.views.detail'),
)
