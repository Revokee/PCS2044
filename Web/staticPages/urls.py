from django.conf.urls import patterns, include, url

urlpatterns = patterns('staticPages.views',
    url(r'^$', 'index', name='index'),
    url(r'index', 'index', name='index'),
    url(r'^mapas/', 'mapas', name='mapas'),
    url(r'^lock', 'lock', name='lock'),
)
