from rest_framework import serializers
from . import models


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = '__all__'


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = '__all__'


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = '__all__'

