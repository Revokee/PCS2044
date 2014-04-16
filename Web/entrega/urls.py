from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #URLS de entrega
    url(r'^entregas.json$','entrega.json.entregas'),
    url(r'^planejamento$','entrega.views.planejamento'),
)
