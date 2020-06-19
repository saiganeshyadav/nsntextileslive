from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Gents,Kids,Suits,Ladies

# Create your views here.

def categories(request,obj):
    if obj=='Gents Wear':
        gents = Gents.objects.all()
        return render(request,'gents.html',{'gents': gents,'cname':obj})
    elif obj=='Kids Wear':
        kids = Kids.objects.all()
        return render(request, 'kids.html',{'kids': kids,'cname':obj})
    elif obj=='Suits':
        suits = Suits.objects.all()
        return render(request,'suits.html',{'suits':suits,'cname':obj})
    elif obj=='Ladies Wear':
        ladies = Ladies.objects.all()
        return render(request,'ladies.html',{'ladies':ladies,'cname':obj})




