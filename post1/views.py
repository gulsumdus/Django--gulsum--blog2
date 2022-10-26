from django.shortcuts import render, HttpResponse #daha kolay anlasilmasi icin httpResponse metodunu cagirdik

# Create your views here.

def post_index(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
     return HttpResponse ('Burası Post index sayfası') 

def post_detail(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
     return HttpResponse ('Burası Post detail sayfası') 

def post_create(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
     return HttpResponse ('Burası Post create sayfası') 

def post_update(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
     return HttpResponse ('Burası Post update sayfası') 

def post_delete(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
     return HttpResponse ('Burası Post delete sayfası') 