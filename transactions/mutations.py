#   MUTATION

from graphene import relay, String, Decimal, Field

from transactions.enums import TransactionType
from transactions.models import Transaction
from transactions.node import TransactionNode


class CreateTransaction(relay.ClientIDMutation):
    transaction = Field(TransactionNode)

    class Input:
        description = String(required=True)
        amount = Decimal(required=True)
        city = String(required=True)
        location = String(required=True)
        transaction_type = TransactionType(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        print(input)
        transaction = Transaction(description = input.get('description'), amount = input.get('amount'), city = input.get('city'), location = input.get('location'), transaction_type = input.get('transaction_type').value)
        transaction.save()
        return CreateTransaction(transaction=transaction)