from django.shortcuts import render, HttpResponse #daha kolay anlasilmasi icin httpResponse metodunu cagirdik
from.models import Post
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
     return render (request,'post\index.html',{'posts':posts}) 



def post_detail(request): 
     post=Post.objects.get(id=2) #id si 2 olan objecti get metoduyla getiriyoruz
      
     context ={                      #post nesnesini icerik olarak gonderme
            'post':post,
     }                                        
     return render(request,'post/detail.html',context) #render fonksiyonu cagırıyoruz ve bunun icine yazilacak bir html sayfası oluşturuyoruz

def post_create(request): 
     return HttpResponse ('Burası Post create sayfası') 

def post_update(request): 
     return HttpResponse ('Burası Post update sayfası') 

def post_delete(request): 
     return HttpResponse ('Burası Post delete sayfası') 