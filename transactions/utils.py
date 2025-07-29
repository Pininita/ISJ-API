# progreso de las transacciones 

from django.db.models import Sum
from .models import Transaction

def get_total_income(user):
    total = Transaction.objects.filter(user=user, transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum']
    return total or 0

def get_total_expense(user):
    total = Transaction.objects.filter(user=user, transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum']
    return total or 0

def get_balance(user):
    income = get_total_income(user)
    expense = get_total_expense(user)
    return income - expense

# NOTA SOBRE aggregate() EN DJANGO:
# 
# Django genera automáticamente las claves para aggregate() usando la convención:
# 'nombre_del_campo__función_de_agregación'
# 
# Ejemplos:
# - Sum('amount') → clave: 'amount__sum'
# - Count('id') → clave: 'id__count'  
# - Avg('price') → clave: 'price__avg'
#
# Si queremos usar un nombre personalizado, podemos hacerlo así:
# Transaction.objects.aggregate(total=Sum('amount'))['total']
# 
# En nuestro caso: aggregate(Sum('amount')) devuelve {'amount__sum': valor}
# Por eso accedemos con ['amount__sum'] y no con ['total']