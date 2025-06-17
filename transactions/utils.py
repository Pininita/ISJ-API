# progreso de las transacciones

from django.db.models import Sum
from .models import Transaction

def get_total_income(user):
    total_income = Transaction.objects.filter(user=user, type='INCOME').aggregate(Sum('amount'))['total'] 
    return total_income or 0

def get_total_expense(user):
    total_expense = Transaction.objects.filter(user=user, type='EXPENSE').aggregate(Sum('amount'))['total']

def get_balance(user):
    income = get_total_income(user)
    expense = get_total_expense(user)
    return income - expense 