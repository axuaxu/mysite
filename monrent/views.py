# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.db.models import Q
from .models import Monrent 

# Create your views here.

def rent(request):
    return render(request, 'monrent/rent.html', {'rent': Monrent.objects.all()})

def nolease(request):
    nl = Monrent.objects.filter(Q(method__contains=u'整租 无租约') | Q(method__contains=u'整租', length__contains=u'可短租'))
    return render(request,'monrent/nolease.html',{'nolease': nl})

