"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from django.contrib import admin
##from post1.views import home_view # hangi viewi kullacagimizi belirttik
#from xml.etree.ElementInclude import include
#from home.views import home_view 
#urlpatterns listesi veb stesindeki adreslerin tanimlandigi yerdir
#urlpatterns = [
 #   url(r'^admin/', admin.site.urls), #admin panali icin adres tanimi
#  url(r'^$',home_view) #anasayfa icin adres taini // '^$'baslangic ve bitis anlamindadir
 #               # virgülden sonra hangi view icin calısacagimizi belirtmeliyiz
#] 


from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_view

urlpatterns = [ 
    url(r'^admin/',admin.site.urls),


    url(r'^$',home_view, name='home'),

    url(r'^post1/', include('post1.urls')), # include ve post1.urls diyerek post1 uyg. url yi referans vermiş olduk 

]