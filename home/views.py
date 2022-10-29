from django.shortcuts import render

def home_view(request): #bir tek argumani olmalıdır 'request', request kullanicilarin istekleri hakkinda bilgi getirir
  #  return HttpResponse ('<b> Hosgeldiniz </b>')
   # return render(request,'home.html',{'isim':'Baris'})#render metodu ile bu isim anahtar çiftini home.html dosyasına aktarıyoruz.
   #alternatif olarak template'e gönderilen değerler birden fazlaysa içerikleri şu şekilde tanımlamak okunabilirliği kolaylaştırır:
    if request.user.is_authenticated():
         context={
    'isim': 'Baris2',
    }
    else:
        context={
              'isim':'Misafir',
        }
    return render(request,'home.html',context)
