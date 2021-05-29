from rest_framework import serializers
from . import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        order = models.Order.objects.create(**validated_data)
        return order

    class Meta:
        model = models.Order
        fields = "__all__"
