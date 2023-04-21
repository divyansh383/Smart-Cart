from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *

# class CompanySerializer(ModelSerializer):
#     employee_count = SerializerMethodField(read_only=True)
#     class Meta:
#         model = Company
#         fields = '__all__'

class UserSerializaer(ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'profile_image']

class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields='__all__'