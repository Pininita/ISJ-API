# progreso de las transacciones 

from django.db.models import Sum
from .models import Transaction

def get_total_income(user):
    total = Transaction.objects.filter(user=user, transaction_type = 'INCOME').aggregate(Sum('amount'))['total'] 
    return total or 0

def get_total_expense(user):
    total = Transaction.objects.filter(user=user, transaction_type = 'EXPENSE').aggregate(Sum('amount'))['total']
    return total or 0

def get_balance(user):
    income = get_total_income(user)
    expense = get_total_expense(user)
    return income - expense 