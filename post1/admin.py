from django.contrib import admin
from.models import Post
# Register your models here.

#ggfds


#admin panelini özelleştirme
class PostAdmin(admin.ModelAdmin):

   list_display = ['title', 'publishing_date'] 
   list_display_links = ['publishing_date'] #linke çevirme =>'title' linkte olursa güncelleme yapılamaz !!
   list_filter = ['publishing_date'] # yayınlanma tarihine göre filtreleme
   search_fields = ['title','content'] #başlık ve metin alanlarına göre arama yapma
   list_editable = ['title']#baslık bigilerini güncelleme 
class Meta:
        model = Post

admin.site.register(Post, PostAdmin)#postadmin classına admin paneli ekledik