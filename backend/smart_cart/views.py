from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from django.urls import reverse

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET'])
def SmartCart_API(request):
    endpoints = {
        'store_data': 'api/items/',
        'set_barcode': 'api/setBarcode',
        'token': 'api/token/',
    }
    return Response(endpoints)

class storeData(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        items=Store.objects.all();
        serializer=StoreSerializer(items,many=True)
        return Response(serializer.data)

class setBarcode(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self, request):
        
        serializer = BarcodeSerializer(data=request.data)
        if serializer.is_valid():
            barcode_id = serializer.validated_data.get('barcode_id')
            try:
                item = Store.objects.get(pk=str(barcode_id))
                serializer=StoreSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Store.DoesNotExist:
                return Response({'error': 'item not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenView(APIView):
    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        refresh_token = RefreshToken(tokens['refresh'])
        access_token = tokens['access']
        return Response({
            'access': str(access_token),
            'refresh': str(tokens['refresh']),
        })
