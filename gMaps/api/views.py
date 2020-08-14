from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework import status


from .models import PropertyAddress,PropertyImage
from .serializers import AddressSerializer

from .utils.convertAddress import reverseAddress

class AddressView(APIView):
    def post(self, request):
        lat = request.data['lat']
        lng = request.data['lng']


        data = reverseAddress(lat, lng)

        if 'description' in request.data:
            data['property_description'] = request.data['description']

        serializer_class = AddressSerializer(data=data)
        print(data)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=200)
        return JsonResponse(serializer_class.errors, status=400)

    def get(self, request, latLong=None):
        if latLong:
            address = Address.objects.filter(latLong=latLong)
        else:
            address = Address.objects.all()
        serializer_class = AddressSerializer(address,many=True)
        return JsonResponse({'status': True, 'msg': 'Succesfully retrived categories', 'data': serializer_class.data},status=200)

class ImageView(APIView):
    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)