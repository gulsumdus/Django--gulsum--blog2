from django.shortcuts import render,HttpResponse

def home_view(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
    return HttpResponse ('<b> Hosgeldiniz </b>')
