from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse

from .model.models import Apartment
from .serializers import ApartmentSerializer

@api_view(['GET'])
def apartment_list(request):
    apartments = Apartment.objects.all()
    serializer=ApartmentSerializer(apartments,many=True)
    
    return JsonResponse(serializer.data, safe=False)