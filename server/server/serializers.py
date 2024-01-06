from rest_framework import serializers
from .model.models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
