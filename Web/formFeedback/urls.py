from django.conf.urls import patterns, include, url
from formFeedback import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^form$', views.formularioFeedback, name='formularioFeedback'),
)