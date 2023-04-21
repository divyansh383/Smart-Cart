from rest_framework import serializers
from .models import *

class UserSerializaer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'profile_image']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields='__all__'

class BarcodeSerializer(serializers.Serializer):
    barcode_id = serializers.CharField(required=True)
