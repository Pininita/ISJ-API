from transactions.constants import transaction_types

TRANSACTION_TYPE_CHOICES = [
        (transaction_types.INCOME, 'Ingreso'),
        (transaction_types.EXPENSE, 'Egreso'),
    ]

# aqui se define los choices que se usaran en enums.py, models.py y donde sea necesario usar los choices