from django.urls import path
from . import views
from .views import *
urlpatterns=[
    path('api/', home),
    path('api/setBarcode/', set_barcode, name='set_barcode'),
    path('api/items/', GetItems.as_view(), name='get_items'),
    path('api/items/<str:barcode_id>/', GetItems.as_view(), name='get_item_by_id'),
  ]