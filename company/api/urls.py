from django.urls import path, include

# from rest_framework import routers
from . import views as ApiViews
from django.conf.urls import url
from rest_framework_nested import routers

# routers = routers.SimpleRouter()
# routers.register("company", ApiViews.CompanyViewSet)

company_router = routers.SimpleRouter()
company_router.register(r"company", ApiViews.CompanyViewSet)

orders_router = routers.NestedSimpleRouter(
    company_router, r"company", lookup="company"
)
orders_router.register(
    r"orders", ApiViews.OrderViewSet, basename="company-order"
)

order_router = routers.SimpleRouter()
order_router.register(r"order", ApiViews.DefaultOrderViewSet)

user_router = routers.SimpleRouter()
user_router.register(r"user", ApiViews.UserViewSet)

urlpatterns = [
    path("", include(company_router.urls)),
    path("", include(orders_router.urls)),
    path("", include(order_router.urls)),
    path("", include(user_router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
