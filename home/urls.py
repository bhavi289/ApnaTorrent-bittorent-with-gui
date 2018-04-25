from django.conf.urls import url, include
from . import views
app_name = 'home'

urlpatterns = [
    url(r'^', views.Home, name='home'),
]
