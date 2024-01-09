from rest_framework import serializers
from .model.models import Apartment, ApartmentBuilding

class ApartmentBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentBuilding
        fields = ['id', 'address', 'admin', 'neighbourhood', 'lat', 'lng']

class ApartmentSerializer(serializers.ModelSerializer):
    building = ApartmentBuildingSerializer()  # Nested serializer for ApartmentBuilding

    class Meta:
        model = Apartment
        fields = ['id', 'name', 'price', 'description', 'area', 'image', 'building']
