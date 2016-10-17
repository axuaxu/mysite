
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /namelist/
    url(r'^$', views.people, name='people'),
]
