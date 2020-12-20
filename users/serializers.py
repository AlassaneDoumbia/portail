
from django.contrib.auth.models import Group
from rest_framework import serializers

from users.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserLimiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, min_length=4)
    new_password = serializers.CharField(required=True, min_length=8)




class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'email': {'read_only': True}
        }


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'password', 'last_name', 'email', 'avatar', 'is_active',
                   'groups', 'modified_by', 'created_by', 'date_joined', 'modified']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'email': {'validators': []},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'modified_by': {'read_only': True},
            'created_by': {'read_only': True},
            'created': {'read_only': True},
            'modified': {'read_only': True}
        }


class AccountEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, min_length=4)
    password = serializers.CharField(required=True, min_length=8)

"""
class AccountPhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, min_length=13, max_length=14)
    password = serializers.CharField(required=True, min_length=8)"""



