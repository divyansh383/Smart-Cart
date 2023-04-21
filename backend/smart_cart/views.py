from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

def home(request):
    return HttpResponse("Hello world")

@api_view(['POST'])
def set_barcode(request):
    barcode_data = request.data.get('barcode')
    
    return Response({'status': 'success'}, status=status.HTTP_200_OK)


# class GetBarcode(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         item = Store.objects.filter(pk=str(pk))
#         serializer = StoreSerializer(item, many=False)
#         return Response(serializer.data)
     
   
class GetItems(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, barcode_id=None):
        if barcode_id:
            item = get_object_or_404(Store, barcode_id=barcode_id)
            serializer = StoreSerializer(item)
            return Response(serializer.data)
        else:
            items = Store.objects.all()
            serializer = StoreSerializer(items, many=True)
            return Response(serializer.data)
