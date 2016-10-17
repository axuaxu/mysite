from django.shortcuts import render
from .models import Monrent 

# Create your views here.

def rent(request):
    return render(request, 'monrent/rent.html', {'rent': Monrent.objects.all()})

