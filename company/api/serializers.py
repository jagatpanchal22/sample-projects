from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Company
        fields = ("url", "pk", "name", "location", "orders")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "pk", "username", "first_name", "last_name", "email")


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    company = CompanySerializer(source="orders", many=True, read_only=True)

    class Meta:
        model = models.Order
        fields = (
            "url",
            "pk",
            "summary",
            "user",
            "company",
            "source",
            "destination",
            "order_date",
        )
        depth = 3
