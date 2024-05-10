from django.contrib import admin
from .models import User
from .serializers import UserSerializer

class UserAdmin(admin.ModelAdmin):
    list_display = 'username',

    def get_tokens(self, obj):
        serializer = UserSerializer(obj)
        return serializer.data['tokens']

    get_tokens.short_description = 'Tokens'

admin.site.register(User, UserAdmin)
