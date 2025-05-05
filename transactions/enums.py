from graphene import Enum

from transactions.choices import TRANSACTION_TYPE_CHOICES
from snipets.graphql.enums import choices_to_enum

TransactionType = Enum('TransactionType', choices_to_enum(TRANSACTION_TYPE_CHOICES))