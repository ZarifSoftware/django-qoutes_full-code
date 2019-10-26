from django.shortcuts import render
from . models import Bangla
from . models import English

def index(request):
    return render(request, "index.html")

def bangla(request):
    b = Bangla.objects.all()
    return render(request, "bangla.html",{'bang':b})

def english(request):
    e = English.objects.all()
    return render(request, "english.html",{'eng':e})

def about(request):
    return render(request, "about.html")

