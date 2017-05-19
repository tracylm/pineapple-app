from django.conf.urls import url
from pineapple import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^happy/', views.happy, name='happy'),
    url(r'^admin/', admin.site.urls), 
]
