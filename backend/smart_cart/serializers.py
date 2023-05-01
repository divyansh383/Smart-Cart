from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields=['email', 'password', 'password2', 'first_name', 'last_name']
    def validate(self, data):
        if(data['password']!=data['password2']):
            raise serializers.ValidationError("Password do not match")
        return data
    def create(self, validated_data):
        validated_data.pop('password2')
        return super().create(validated_data)
    
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


class AddToCartSerializer(serializers.Serializer):
    barcode_id = serializers.CharField(required=True)

