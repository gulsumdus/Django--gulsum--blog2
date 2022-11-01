
from django.conf.urls import url
from .views import *




urlpatterns = [
    
    url(r'^index/$',post_index), #temel post işlemleri için adres tanimi
    url(r'^(?P<id1>\d+)$',post_detail),#tek bir adresi değil istenilen adresin id'sini otomatik adresler// post/views.py da da bu argumanı /id1)göndermeliyiz
    url(r'^creat/$',post_create),
    url(r'^update/$',post_update),
    url(r'^delete/$',post_delete),

    ]