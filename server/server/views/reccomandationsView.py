from django.http import JsonResponse
from math import radians, sin, cos, sqrt, atan2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.models import Apartment
from ..serializers import ApartmentSerializer

class ReccomandationsListCreateView(APIView):

    def calculate_score(location, price)

    def __haversine(self, lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c

    def get(self, request, *args, **kwargs):
        accommodations = Apartment.objects.all()
        serializer = ApartmentSerializer(accommodations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
