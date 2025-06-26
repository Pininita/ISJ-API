#   MUTATION

from graphene import relay, String, Decimal, Field
from graphql import GraphQLError
from graphql_jwt.decorators import login_required
from graphql_relay import from_global_id

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
        user_id = String(required=True)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **input):

        print(input.get("transaction_type").value)

        _, user_id = from_global_id(input.get("user_id"))

        print(user_id)

        print(info.context.user.id)

        print(user_id != info.context.user.id)

        # if user_id != info.context.user.id:
        #     raise GraphQLError("You are not authorized to perform this action.")

        transaction = Transaction.objects.create(
            description = input.get('description'),
            amount = input.get('amount'),
            city = input.get('city'),
            location = input.get('location'),
            transaction_type = input.get('transaction_type').value,
            user_id= user_id
        )

        return CreateTransaction(transaction=transaction)