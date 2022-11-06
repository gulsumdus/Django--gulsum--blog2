from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model): #model k�t�phanesinden model class� �a��rd�k
    title=models.CharField(max_length=120, verbose_name='baslik')
    content=models.TextField(verbose_name='Icerik')
    publishing_date=models.DateTimeField(verbose_name='Yayinlanma Tarihi',auto_now_add=True)

    def __str__(self):
        return self.title                        #eklenen postun basligi  neyse onu gosteririr
    def get_absolute_url(self):
        return reverse('post_1:detail',kwargs={'id':self.id})
       #  return "/post/{}".format(self.id)#bu fnksiyon hangi post nesnesinde cagrildiysa onun adresini hesaplar.
#diger url adresleri icin de adres metodlari olusturuyoruz..
    def get_create_url(self):
        return reverse('post_1:create')#create icin arguman vermemize gerek yok

    def get_update_url(self):
        return reverse('post_1:update',kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('post_1:delete',kwargs={'id':self.id})