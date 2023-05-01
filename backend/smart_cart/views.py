from rest_framework.decorators import api_view
from django.http import HttpResponse

from . models import *
from . serializers import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from rest_framework import generics

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

        'access token': 'api/token/',
        'refresh token': 'api/token/refresh',


    }
    return Response(endpoints)


class createUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
        

class userDataView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user


class storeData(APIView):
    permission_classes = [IsAuthenticated|IsAdminUser|IsAuthenticatedOrReadOnly]

    #authentication_classes=[JWTAuthentication]
    def get(self,request):
        items=Store.objects.all();
        serializer=StoreSerializer(items,many=True)
        return Response(serializer.data)

class setBarcode(APIView):
    #permission_classes = [IsAuthenticated]
    #authentication_classes=[JWTAuthentication]
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

class AssignCart(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        # uid=int(request.data['user_id']);
        user=request.user
        cid=int(request.data['cart_id']);
        if(Cart_User.objects.filter(cart_id=cid, user_id=user).exists()):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        assignedCart=Cart_User.objects.create(cart_id=cid,user_id=user);
        try:
            assignedCart.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
