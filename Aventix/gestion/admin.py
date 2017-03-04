from django.contrib import admin
from .models import Transaction, Commercant, Employe, Employeur, Recharge, Carte

# Register your models here.

admin.site.register(Employe)
admin.site.register(Employeur)
admin.site.register(Commercant)
admin.site.register(Transaction)
admin.site.register(Recharge)
admin.site.register(Carte)
