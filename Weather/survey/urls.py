from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<participant_id>[0-9]+)/$', views.index, name='index'),
	url(r'^(?P<participant_id>[0-9]+)/example$', views.example, name='example'),
	url(r'^(?P<participant_id>[0-9]+)/trial$', views.trial, name='trial')
]
