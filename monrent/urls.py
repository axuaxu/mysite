
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /monrent/
    url(r'^$', views.rent, name='rent'),
    # ex: /monrent/nolease/
    url(r'^nolease/$',views.nolease, name='nolease'),
]

