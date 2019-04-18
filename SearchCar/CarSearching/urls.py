from django.conf.urls import url
from CarSearching import views

app_name = 'CarSearching'
urlpatterns = [
  # The home view ('/CarSearching/')
  url(r'^$', views.home, name='layout'),
  url(r'^layout/$', views.home, name='layout'),
  url(r'^car_list/$', views.car_list, name='car_list'),
  url(r'^framec/$', views.framec, name='framec')
]