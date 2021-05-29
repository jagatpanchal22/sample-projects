from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.Companies.as_view()),
    path('company/<str:company_id>/', views.CompanyDetail.as_view()),
    path('company/<str:company_id>/orders/', views.Orders.as_view()),
    path('company/<str:company_id>/orders/<str:order_id>/', views.OrderDetail.as_view()),
]