from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.appmain, name='appmain'),
	url(r'^get/$', views.appmain, name='uranai'),
	#url(r'^get/$', views.appmain, name='test')
]
