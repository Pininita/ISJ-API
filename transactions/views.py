from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionsSerializer