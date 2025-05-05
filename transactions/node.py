from graphene import relay
from graphene_django import DjangoObjectType

from transactions.models import Transaction

# expongo los datos basicos que quiero que muestre graphene

class TransactionNode(DjangoObjectType):
    class Meta:
        model = Transaction
        filter_fields = []
        interfaces = (relay.Node,)
