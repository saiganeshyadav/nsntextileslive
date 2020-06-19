from django.shortcuts import render
from .models import Items
# Create your views here.

def home(request):
    items = Items.objects.all()
    return render(request, 'home.html', {'items': items})
