
from django.conf.urls import url
from .views import *

app_name= 'post1' #karisikliklari onlemek icin app_name tanimladik


urlpatterns = [
    
    url(r'^index/$',post_index,name='index_1'), #temel post işlemleri için adres tanimi
    url(r'^(?P<id1>\d+)/$',post_detail,name='detail_1'),#tek bir adresi değil istenilen adresin id'sini otomatik adresler// post/views.py da da bu argumanı /id1)göndermeliyiz
    url(r'^creat/$',post_create, name='create_1'),
    url(r'^update/$',post_update, name='update_1'),
    url(r'^delete/$',post_delete, name='delete_1'),

    ]