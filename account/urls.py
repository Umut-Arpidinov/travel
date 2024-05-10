from django.urls import path
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/register/', UserViewSet.as_view({'post': 'register'})),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'view_profile'})),
    path('users/info/', UserViewSet.as_view({'get': 'user_info_by_token'})),
    path('users/', UserViewSet.as_view({'get': 'list_users'})),    
]

urlpatterns += router.urls
