from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Company
        fields = ('url', 'pk', 'name', 'location')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'first_name', 'last_name', 'email')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = models.Order
        fields = ('url', 'pk', 'summary', 'company', 'user', 'source', 'destination', 'order_date')
        depth = 3
