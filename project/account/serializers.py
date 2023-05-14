from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('email','password','first_name','last_name')


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        models = User
        fields = ('email','password','first_name','last_name')


    def create(self,validate_data):
        user = User.objects.create_user(
            email=validate_data['email'],
            password=validate_data['password'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],

        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password= serializers.CharField()

    def validate(self,attrs):
        user = authenticate(email=attrs['email'],password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid email or password')
        attrs['user'] = user
        return attrs

    def to_representation(self, instance):
        response_data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        response_data['access_token']= str(refresh.access_token)
        response_data['refresh_token']=str(refresh)
        response_data['user_id'] = instance.id
        return response_data
#purpose of to_representation


