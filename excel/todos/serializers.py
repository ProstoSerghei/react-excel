from rest_framework.serializers import Field, CurrentUserDefault, ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User

from .models import Todo



class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'url']


class TodoModelSerializer(ModelSerializer):
    user = UserModelSerializer(read_only=True)
    user_id = PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    class Meta:
        model = Todo
        fields = '__all__'