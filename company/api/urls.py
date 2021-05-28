from django.urls import path, include
# from rest_framework import routers
from . import views as ApiViews
from django.conf.urls import url
from rest_framework_nested import routers

# routers = routers.SimpleRouter()
# routers.register("company", ApiViews.CompanyViewSet)

router = routers.SimpleRouter(trailing_slash=False)
router.register('company', ApiViews.CompanyViewSet)

order_router = routers.NestedSimpleRouter(router, r'company', lookup='company')
order_router.register(r'order', ApiViews.OrderViewSet, basename='company-order')

# routers.register(r"order", ApiViews.OrderViewSet)
# routers.register(r"user", ApiViews.UserViewSet)
app_name = 'company'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(order_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # Get list of orders in a company
    # url(r'^company/(?P<library_pk>\w+)/Order/?$', ApiViews.OrderViewSet.as_view({'get': 'list'}),
    #     name='company-order-list'),
    # # Get details of a order in a company
    # url(r'^company/(?P<library_pk>\w)/Order/(?P<pk>\w)/?$', ApiViews.OrderViewSet.as_view({'get': 'retrieve'}),
    #     name='company-order-detail')
]