from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.models import Apartment
from ..serializers import ApartmentSerializer

class ApartmentListCreateView(APIView):
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
