from django.db import models

# Create your models here.

class Post(models.Model): #model k�t�phanesinden model class� �a��rd�k
    title=models.CharField(max_length=120, verbose_name='baslik')
    content=models.TextField()
    publishing_date=models.DateTimeField()

    def __str__(self):
        return self.title                        #eklenen postun basligi  neyse onu gosteririr
  