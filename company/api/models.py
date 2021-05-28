from django.db import models
from django.contrib.auth.models import User
import uuid


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    location = models.CharField(max_length=200, verbose_name="Location")

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
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS)
    order_by = models.ForeignKey(
        Company,
        related_name="orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    managed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.summary
