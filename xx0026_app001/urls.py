from django.conf.urls import url

from xx0026_app001 import views


urlpatterns= [
	url(r'^$', views.index, name= 'index')

]