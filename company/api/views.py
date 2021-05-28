from .models import Company, Order
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CompanySerializer, OrderSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.http import Http404


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DefaultOrderViewSet(viewsets.ModelViewSet):
    """Viewset of Order"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        company_id = self.kwargs["company_pk"]
        try:
            return Order.objects.filter(order_by=company_id)
        except Order.DoesNotExist:
            raise Http404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
