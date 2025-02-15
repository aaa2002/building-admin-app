from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse, HttpResponse
import base64
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.templatetags.static import static
from django.contrib.staticfiles import finders
from .model.models import Apartment, ApartmentBuilding
from .serializers import ApartmentSerializer, ApartmentBuildingSerializer
from .forms import ApartmentBuildingForm, ApartmentForm
from math import radians, sin, cos, sqrt, atan2

# @api_view(['GET'])
# def apartment_list(request):
#     apartments = Apartment.objects.all()
#     serializer=ApartmentSerializer(apartments,many=True)
    
#     return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def apartment_list(request):
    user_lat = float(request.data['lat'])
    user_lon = float(request.data['lon'])

    # Function to calculate distance using Haversine formula
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    apartments = Apartment.objects.all()

    # Calculate distances and add to apartments
    distances = []
    for apartment in apartments:
        distance = haversine(user_lat, user_lon, apartment.building.lat, apartment.building.lng)
        distances.append((apartment, distance))

    # Sort apartments by distance
    sorted_apartments = sorted(distances, key=lambda x: x[1])

    # Extract only the apartments from the sorted list
    sorted_apartments = [apartment[0] for apartment in sorted_apartments]

    serializer = ApartmentSerializer(sorted_apartments, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def apartment_building_list(request):
    apartment_buildings = ApartmentBuilding.objects.all()
    serializer = ApartmentBuildingSerializer(apartment_buildings,many=True)
    
    return JsonResponse(serializer.data, safe=False)

import os

@api_view(['GET'])
def apartment_get(request, name):
    # Get the name from the request parameters
    name = name
    if not name:
        return JsonResponse({"error": "Name parameter is required"}, status=400)

    try:

        apartment = Apartment.objects.get(name=name)
        
        serializer = ApartmentSerializer(apartment)
        serialized_data = serializer.data


        return JsonResponse({"apartment": serialized_data}, safe=False)
    except Apartment.DoesNotExist:
        return JsonResponse({"error": "Apartment not found"}, status=404)
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_apartment_image(request, name):
    apartment = get_object_or_404(Apartment, name=name)
    image_path = os.path.join(settings.MEDIA_ROOT, str(apartment.image))
    with open(image_path, 'rb') as image_file:
        return HttpResponse(image_file.read(), content_type='image/jpeg')
    
@api_view(['POST'])
def add_apartment_building(request):
    data = request.data
    messages = 'success'
    form = ApartmentBuildingForm({
        'address' : data.get('address'),
        'admin' : data.get('admin'),
        'neighbourhood' : data.get('neighbourhood'),
        'lat' : data.get('lat'),
        'lng' : data.get('lng'),
    })
    if form.is_valid():
        form.save()
    else: 
        print(form)
        messages = 'error'
    return JsonResponse({'message':messages})

@api_view(['POST'])
def add_apartment(request):
    data = request.data
    messages = 'success'
    form = ApartmentForm({
        'name' : data.get('name'),
        'price' : data.get('price'),
        'description' : data.get('description'),
        'area' : data.get('area'),
        'image' : data.get('image'),
        'building' : data.get('building'),
    })
    if form.is_valid():
        form.save()
    else: 
        print(form)
        messages = 'error'
    return JsonResponse({'message':messages})
    