from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^novo_pedido/','orderGrouping.views.create_order'),
    url(r'^pedidos/','orderGrouping.views.orders'),
    url(r'^deletar_pedido/(?P<order_id>[0-9]+)/$', 'orderGrouping.views.delete_order'),
    url(r'^', include('staticPages.urls', namespace="staticPages")),
    #url(r'', 'staticPages.views.home'),
    # Examples:
    # url(r'^$', 'PCS2044.views.home', name='home'),
    # url(r'^PCS2044/', include('PCS2044.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^novo_pedido/','orderGrouping.views.create_order'),
)
