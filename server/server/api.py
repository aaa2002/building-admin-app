from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse

from .model.models import Apartment
from .serializers import ApartmentSerializer

@api_view(['GET'])
def apartment_list(request):
    apartments = Apartment.objects.all()
    serializer=ApartmentSerializer(apartments,many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def apartment_get(request,name):
    # Get the name from the request parameters
    name = name
    if not name:
        return JsonResponse({"error": "Name parameter is required"}, status=400)

    try:
        # Retrieve the Apartment object with the specified name
        apartment = Apartment.objects.get(name=name)
        serializer = ApartmentSerializer(apartment)
        return JsonResponse({"apartment": serializer.data}, safe=False)
    except Apartment.DoesNotExist:
        return JsonResponse({"error": "Apartment not found"}, status=404)