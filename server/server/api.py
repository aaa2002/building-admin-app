from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse, HttpResponse
import base64
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.templatetags.static import static
from django.contrib.staticfiles import finders
from .model.models import Apartment
from .serializers import ApartmentSerializer
from .forms import ApartmentBuildingForm, ApartmentForm

@api_view(['GET'])
def apartment_list(request):
    apartments = Apartment.objects.all()
    serializer=ApartmentSerializer(apartments,many=True)
    
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
    