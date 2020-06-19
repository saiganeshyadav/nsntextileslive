from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Gshirts,Gpants,Gtshirts,Kshirts,Kpants,Kshirtspants,Sherwani,Ksuits,Kdothi,Lleggins,Ldresses

def materials(request,obj):
    if obj=='SHIRTS':
        gshirts=Gshirts.objects.all()
        return render(request,'gshirts.html',{'gshirts':gshirts,'mname':obj})
    elif obj=='TROUSERS':
        gpants=Gpants.objects.all()
        return render(request,'gpants.html',{'gpants':gpants,'mname':obj})
    elif obj=='T-SHIRTS':
        gtshirts=Gtshirts.objects.all()
        return render(request,'gt-shirts.html',{'gtshirts':gtshirts,'mname':obj})
    elif obj=='SHIRTS(KIDS)':
        kshirts=Kshirts.objects.all()
        return render(request,'kshirts.html',{'kshirts':kshirts,'mname':obj})
    elif obj=='PANTS':
        kpants = Kpants.objects.all()
        return render(request,'kpants.html',{'kpants':kpants,'mname':obj})
    elif obj=='SHIRTS,PANTS(MIXED)':
        kshirtspants=Kshirtspants.objects.all()
        return render(request,'kshirts,pants.html',{'kshirtspants':kshirtspants,'mname':obj})
    elif obj=='SHERWANI':
        sherwani=Sherwani.objects.all()
        return render(request,'ksherwani.html',{'sherwani':sherwani,'mname':obj})
    elif obj=='SUITS':
        ksuits=Ksuits.objects.all()
        return render(request,'ksuits.html',{'ksuits':ksuits,'mname':obj})
    elif obj=='DOTHI':
        kdothi=Kdothi.objects.all()
        return render(request,'kdothi.html',{'kdothi':kdothi,'mname':obj})
    elif obj=='LEGGINS':
        lleggins=Lleggins.objects.all()
        return render(request,'leggins.html',{'lleggins':lleggins,'mname':obj})
    elif obj=='DRESSES':
        ldresses=Ldresses.objects.all()
        return render(request,'dresses.html',{'ldresses':ldresses,'mname':obj})



