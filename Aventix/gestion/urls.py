from django.conf.urls import url
from . import views

app_name = 'gestion'

urlpatterns = [
    url(r'^transactions/$', views.transactions, name='transactions'),
    url(r'^solde/$', views.solde, name='solde'),
]
