
from django.conf.urls import url
from .views import *




urlpatterns = [
    
    url(r'^index/$',post_index), #temel post işlemleri için adres tanimi
    url(r'^detail/$',post_detail),
    url(r'^creat/$',post_create),
    url(r'^update/$',post_update),
    url(r'^delete/$',post_delete),

    ]