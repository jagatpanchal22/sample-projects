from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create", views.short, name="home"),
    path("<str:pk>", views.go, name="home"),
]
