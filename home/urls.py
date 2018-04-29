from django.conf.urls import url, include
from . import views
app_name = 'home'

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^downloading', views.Downloading, name='downloading'), 
    url(r'^download-percentage', views.DownloadPercentage, name='download-percentage'), 


]
