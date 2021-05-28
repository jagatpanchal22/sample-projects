from .models import Company, Order
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CompanySerializer, OrderSerializer, UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Viewset of Order"""
    queryset = Order.objects.all().select_related('order_by').prefetch_related('users')
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        company_id = self.kwargs.get("order_by")
        print(company_id)
        return None
        # try:
        #     company = Company.objects.get(id=company_id)
        # except Company.DoesNotExist:
        #     raise NotFound('A Company with this id does not exist')
        # return self.queryset.filter(order_by=company)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
