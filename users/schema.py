import graphene
from graphql_jwt.decorators import login_required
from graphql_jwt import Verify, Refresh, \
    ObtainJSONWebToken
from users.nodes import UserNode
from django.contrib.auth import get_user_model


User = get_user_model()

# aca estoy mostrando en el playground la accecibilidad para ver la informacion de los usuarios pero
# con un fin de practica, lo ideal es que no se pueda ver la informacion del usuario y que solo
# la pueda ver el admin, por esa razon en la class Query se comentaron dos lienas
# el 'me' permite al usuario que esta loguiado, revisar su propia informacion

class Query(graphene.ObjectType): #para obtener los datos del usuario autenticado
    me = graphene.Field(UserNode)
    # users = DjangoFilterConnectionField(UserNode)
    # user = relay.Node.Field(UserNode)

    @login_required
    def resolve_me(self, info):
        user = info.context.user
        return user

    @login_required
    def resolve_users(self, info):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        phone = graphene.String(required=False)

    def mutate(self, info, username, email, password, first_name=None, last_name=None, phone=None):
        user = User(
            username=username,
            email=email,
            first_name=first_name if first_name else "",
            last_name=last_name if last_name else "",
            phone=phone if phone else "",
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Arguments:
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    @login_required
    def mutate(self, info, email=None, first_name=None, last_name=None):
        user = info.context.user

        if email:
            user.email = email
        if first_name:
            user.first_name =  first_name
        if last_name:
            user.last_name = last_name

        user.save()
        return UpdateUser(user=user)

class ChangePassword(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        old_password = graphene.String(required=True)
        new_password = graphene.String(required=True)

    @login_required
    def mutate(self, info, old_password, new_password):
        user = info.context.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return ChangePassword(success=True)
        return ChangePassword(success=False)

class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    change_password = ChangePassword.Field()