from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','email', 'first_name', 'last_name', 'profile_image']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields='__all__'

class BarcodeSerializer(serializers.Serializer):
    barcode_id = serializers.CharField(required=True)

class CartSerializer(serializers.ModelSerializer):
    item = StoreSerializer()

    class Meta:
        model = Cart
        fields = '__all__'
class CartUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Cart_User
        fields='__all__'



