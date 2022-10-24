from django.shortcuts import render, HttpResponse #daha kolay anlasilmasi icin httpResponse metodunu cagirdik

# Create your views here.

def home_view(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
    return HttpResponse ('<b> Hosgeldiniz </b>')