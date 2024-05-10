from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action != 'user_info_by_token':
            return True
        return request.user and request.user.is_authenticated
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomPermission]

    @action(detail=True, methods=['get'])
    def view_profile(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def list_users(self, request):
        queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def user_info_by_token(self, request):
        username = request.GET.get('username')
        email = request.GET.get('email')
        user_data = {
            'username': username,
            'email': email,
        }
        return Response(user_data)
    