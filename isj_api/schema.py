import graphene
import transactions.schema
import graphql_jwt
import users.schema
from users.schema import Query as UserQuery, Mutation as UserMutation

class Query(users.schema.Query ,transactions.schema.Query, graphene.ObjectType):
    pass

class Mutation(
    users.schema.Mutation ,
    transactions.schema.Mutation,
    graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=graphene.Schema(query=Query, mutation=Mutation)