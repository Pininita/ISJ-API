from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from .models import Transaction
from .mutations import CreateTransaction
from .node import TransactionNode


# QUERY & MUTATION

class Query(ObjectType):
    transactions = DjangoFilterConnectionField(TransactionNode)
    transaction = relay.Node.Field(TransactionNode) # para consultar un id

    @login_required
    def resolve_transactions(self, info, **kwargs):
        user = info.context.user
        return Transaction.objects.filter(user=user)


class Mutation(ObjectType):
    create_transaction = CreateTransaction.Field()