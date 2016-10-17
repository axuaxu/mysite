from django.shortcuts import render
from .models import Person
# Create your views here.


def people(request):
    return render(request, 'namelist/people.html', {'people': Person.objects.all()})
