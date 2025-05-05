from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionsViewSet # cuando uso . me refiero en mi mismo directorio

router = DefaultRouter()
router.register('transactions', TransactionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]