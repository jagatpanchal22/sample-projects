from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<str:pk>/', views.CompanyDetail.as_view()),
    path('company/<str:company_id>/orders/', views.OrderList.as_view()),
    path('company/<str:company_id>/orders/<str:pk>/', views.OrderDetail.as_view()),
]