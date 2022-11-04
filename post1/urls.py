
from django.conf.urls import url
from .views import *

app_name= 'post_1' #karisikliklari onlemek icin app_name tanimladik


urlpatterns = [
    
    url(r'^index/$',post_index,name='index'), #temel post işlemleri için adres tanimi
    url(r'^(?P<id>\d+)/$',post_detail,name='detail'),#tek bir adresi değil istenilen adresin id'sini otomatik adresler// post/views.py da da bu argumanı /id1)göndermeliyiz
    url(r'^create/$',post_create, name='create'),
    url(r'^update/$',post_update, name='update'),
    url(r'^delete/$',post_delete, name='delete'),

    ]