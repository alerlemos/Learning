from django.conf.urls import url
from django.urls.resolvers import URLPattern
from first_app import views


urlpatterns = [
    url('', views.index, name='index'),
]