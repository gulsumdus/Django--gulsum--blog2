from django.shortcuts import render, HttpResponse,get_object_or_404#daha kolay anlasilmasi icin httpResponse metodunu cagirdik
  #error control'u import ettik
from.models import Post
from.forms import PostForm #forms.py deki PostForm classını import ettik
# Create your views here.

#def post_index(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
 #    return HttpResponse ('Burası Post index sayfası') 

#def post_detail(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
 #    return HttpResponse ('Burası Post detail sayfası') 

#def post_create(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
 #    return HttpResponse ('Burası Post create sayfası') 

#def post_update(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
 #    return HttpResponse ('Burası Post update sayfası') 

#def post_delete(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
 #    return HttpResponse ('Burası Post delete sayfası') 

def post_index(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
     posts=Post.objects.all() #posttaki oluşrueulmuş bütün objectleri listeler
     context={
          'posts':posts,
     }
     return render (request,'post/index.html',context) 



def post_detail(request, id):# id1 argumanı post1/urls.py da tanımladık ve bunu aşağıdaki get metodunda uyguluyoruz
     #post=Post.objects.get(id=2) #id si 2 olan objecti get metoduyla getiriyoruz
     post = get_object_or_404(Post, id=id)# id'si 2 olanı değil artık diğer bütün id lere id1 üzerinden ulaşırız... 
     context ={                      #post nesnesini icerik olarak gonderme
            'post':post,
     }                                        
     return render(request,'post/detail.html',context) #render fonksiyonu cagırıyoruz ve bunun icine yazilacak bir html sayfası oluşturuyoruz

def post_create(request): 
     #form=PostForm()//serverdan gönderilen form biligilerini almak icin asagida kulllanacagiz

     # 2 alternative sekilde formdan alinan bilgilerle post obj olusturabiliriz:

     #1
     if request.method=='POST':
          form=PostForm(request.POST)#formdan bilgileri kaydeder.
          if form.is_valid():#kontrol eder
               form.save()
     else:
          #formu kullaniciya goster
          form=PostForm()
     #2
     form=PostForm(request.POST or None)#requestpost dolu gelirse parametre olarak al değilse alma demektirr
     if form.is_valid():
          form.save()
     context={
          'form':form,
     }
     #if request.method == "POST": 
         # #print komutu ile serverin calistiği komut ekranina gelen post istegini yazdiriyor
      #    print(request.POST)
     return render(request,'post/form.html',context)

def post_update(request): 
     return HttpResponse ('Burası Post update sayfası') 

def post_delete(request): 
     return HttpResponse ('Burası Post delete sayfası') 