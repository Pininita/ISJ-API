from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from .models import Transaction
from .mutations import CreateTransaction
from .node import TransactionNode


# QUERY & MUTATION

class Query(ObjectType):
    transactions = DjangoFilterConnectionField(TransactionNode)
    transaction = relay.Node.Field(TransactionNode) # para consultar un id

    def resolve_transactions(self, info, **kwargs):
        user = info.context.user
        if not user:
            raise GraphQLError('You must be logged in to view this page.')
        return Transaction.objects.filter(user_id=user.id)


class Mutation(ObjectType):
    create_transaction = CreateTransaction.Field()