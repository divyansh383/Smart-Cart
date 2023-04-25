from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from django.urls import reverse

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import  authentication_classes, permission_classes


@api_view(['GET'])
def SmartCart_API(request):
    endpoints = {
        'store_data': 'api/items/',
        'set_barcode': 'api/setBarcode',
        'token': 'api/token/',
    }
    return Response(endpoints)

class storeData(APIView):
    permission_classes = [IsAuthenticated|IsAdminUser|IsAuthenticatedOrReadOnly]

    #authentication_classes=[JWTAuthentication]
    def get(self,request):
        items=Store.objects.all();
        serializer=StoreSerializer(items,many=True)
        return Response(serializer.data)

class setBarcode(APIView):
<<<<<<< HEAD
    #permission_classes = [IsAuthenticated]
    #authentication_classes=[JWTAuthentication]
=======
    # permission_classes = [IsAuthenticated]
    # authentication_classes=[JWTAuthentication]
>>>>>>> origin/avinash
    def post(self, request):
        serializer = BarcodeSerializer(data=request.data)
        if serializer.is_valid():
            barcode_id = serializer.validated_data.get('barcode_id')
            try:
                item = Store.objects.get(pk=str(barcode_id))
                serializer = StoreSerializer(item)
                print("barcode -------------", barcode_id)

                cart_item, created = Cart.objects.get_or_create(item=item)
                if created:
                    cart_item.quantity = 1
                    cart_item.save()
                    cart_serializer = CartSerializer(cart_item)
                    response_data = {
                        'item_details': serializer.data,
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    response_data = {
                        'item_details': 'Item already scanned',
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
            except Store.DoesNotExist:
                print('Item does not exit in store')
                return Response({'error': 'item not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            print("serializer is not valid")
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


#------------------------------------------------------------------------------
@api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        barcode_id = serializer.validated_data['barcode_id']
        try:
            store_item = Store.objects.get(pk=barcode_id)
            cart_item, created = Cart.objects.get_or_create(item=store_item)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            serializer = CartSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Store.DoesNotExist:
            return Response({'error': 'item not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
