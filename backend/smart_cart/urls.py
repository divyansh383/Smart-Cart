from django.urls import path
from .views import *

urlpatterns = [
    path('api/', SmartCart_API),
    path('api/items/', storeData.as_view(), name='store-data'),
    path('api/setBarcode/', setBarcode.as_view(), name='set-barcode'),
    path('api/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('api/token/', TokenView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
