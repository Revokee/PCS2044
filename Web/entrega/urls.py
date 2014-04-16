from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #URLS de entrega
    url(r'^entregas.json$','entrega.js.entregas'),
    url(r'^planejamento$','entrega.views.planejamento'),
    url(r'^planejamento$','entrega.views.planejamento'),
    url(r'^login$', 'entrega.mobile.login'),
    url(r'^push_location$', 'entrega.mobile.push_location'),

)
