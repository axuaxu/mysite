# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Monrent

# Register your models here.

class MonrentAdmin(admin.ModelAdmin):
     list_display = ('num','udate','title','address','pcode','rent','rooms','rstyle','intime','method','length')
     list_filter = ('method','length','rooms','pcode')


admin.site.register(Monrent,MonrentAdmin)
