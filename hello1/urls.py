from django.conf.urls import url
from hello1 import views




urlpatterns = [
    url(r'^$', views.index, name= 'index' ),
       
]