from graphene import relay, Float
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from transactions.enums import TransactionTypeEnum

from transactions.models import Transaction

User = get_user_model()

# class PersonType(ObjectType):
#    name = String()

class UserNode(DjangoObjectType):
    balance = Float()
    total_income = Float()
    total_expense = Float()

    class Meta:
        model = User
        filter_fields = []
        interfaces = (relay.Node,)


    def resolve_balance(self, info):
        user = self
        trans = self.transactions.all()
        print(trans)
        transactions = Transaction.objects.filter(user=user)
        print(transactions)

        total = 0
        for transaction in transactions:
            print("Transaction -> ", transaction)
            if transaction.transaction_type == TransactionTypeEnum.IN.value:
                print("Es un ingreso")
                total += transaction.amount
            if transaction.transaction_type == TransactionTypeEnum.OUT.value:
                print("Es un egreso")
                total -= transaction.amount
        return float(total)

    def resolve_total_income(self, info):
        user = self
        trans = self.transactions.all()
        transactions = Transaction.objects.filter(user=user)

        total = 0
        for transaction in transactions:
            if transaction.transaction_type == TransactionTypeEnum.IN.value:
                total += transaction.amount
        return float(total)

    def resolve_total_expense(self, info):
        user = self
        trans = self.transactions.all()
        transactions = Transaction.objects.filter(user=user)

        total = 0
        for transaction in transactions:
            if transaction.transaction_type == TransactionTypeEnum.OUT.value:
                total += transaction.amount
        return float(total)
