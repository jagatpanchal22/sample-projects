from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=120, unique=True, verbose_name="Company Name"
    )
    location = models.CharField(max_length=120, verbose_name="Address")

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_STATUS = [
        ("OPEN", "Ordered"),
        ("SHIPPED", "In Shipping"),
        ("CANCELLED", "Cancelled"),
        ("DELIVERED", "Delivered"),
        ("RETURNED", "Returned"),
        ("PENDING", "Pending"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    summary = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=120, null=False, blank=False)
    destination = models.CharField(max_length=120, null=False, blank=False)
    by_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0]
    )
    managed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, default="1"
    )

    def __str__(self):
        return self.summary
