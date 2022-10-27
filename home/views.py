from django.shortcuts import render

def home_view(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
  #  return HttpResponse ('<b> Hosgeldiniz </b>')
    return render(request,'home.html',{})
