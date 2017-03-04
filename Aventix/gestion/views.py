from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from .models import Commercant, Employe, Carte, Transaction

# Create your views here.


def transactions(request):
    if request.user.is_authenticated():
        user = request.user
        historique = Transaction.objects.filter(id_commercant=user.id)
        context = {
                'user': request.user,
                'historique': historique,
                }
        return render(request, 'gestion/transactions.html', context)
    else:
        return render(request, 'gestion/')


def solde(request):
    if request.user.is_authenticated():
        carte = Carte.objects.get(id=Employe.num_carte)
        context = {
                'user': request.user,
                'solde': carte.solde,
                }
        return render(request, 'gestion/solde.html', context)
    else:
        return render(request, 'gestion/')
