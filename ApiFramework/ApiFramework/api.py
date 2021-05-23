from rest_framework import routers
from rental import api_views as ApiViews


routers = routers.DefaultRouter()
routers.register(r"friends", ApiViews.FriendViewSet)
routers.register(r"belongings", ApiViews.BelongingViewSet)
routers.register(r"borrowings", ApiViews.BorrowedViewSet)
