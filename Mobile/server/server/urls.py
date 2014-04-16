from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login$', 'middleware.models.login'),
    url(r'^push_location$', 'middleware.models.push_location'),

    url(r'^admin/', include(admin.site.urls)),
)
