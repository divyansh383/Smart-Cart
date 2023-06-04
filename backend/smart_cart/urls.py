from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.SmartCart_API),
    path('api/items/', views.storeData.as_view(), name='store-data'),
    path('api/setBarcode/', views.setBarcode.as_view(), name='set-barcode'),
    path('api/token/', views.TokenView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verifyUser/',views.userDataView.as_view()),
    path('api/createUser/',views.createUserView.as_view()),
    path('api/assign-user/',views.AssignCart.as_view()),
    path('api/getCartItems',views.ShowCart.as_view())
]
