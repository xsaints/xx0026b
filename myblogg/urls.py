from django.conf.urls import url

from myblogg import views


urlpatterns= [
  url('^$', views.index, name= "index"),
  url('^help/$', views.help, name= "help"),
]