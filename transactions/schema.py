from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Transaction
from .mutations import CreateTransaction
from .node import TransactionNode


# QUERY & MUTATION

class Query(ObjectType):
    transactions = DjangoFilterConnectionField(TransactionNode)
    transaction = relay.Node.Field(TransactionNode) # para consultar un id


class Mutation(ObjectType):
    create_transaction = CreateTransaction.Field()