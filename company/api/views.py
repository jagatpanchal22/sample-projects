from .models import Company, Order
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CompanySerializer, OrderSerializer, UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer


class DefaultOrderViewSet(viewsets.ModelViewSet):
    """Viewset of Order"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Viewset of Order"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # return None

    def get_queryset(self, *args, **kwargs):
        company_id = self.kwargs['company_pk']
        try:
            orders = Order.objects.filter(order_by=company_id)
            print(orders)
            # print(orders)
            # result = OrderSerializer(data=orders, context={'request': self.request}).is_valid()
            # print(result)
            # print(result.data)
        except Order.DoesNotExist:
            raise NotFound('No order placed')
        return orders


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
