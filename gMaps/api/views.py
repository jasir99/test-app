from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Address
from django.forms.models import model_to_dict
from .serializers import AddressSerializer
from rest_framework.parsers import MultiPartParser

from .utils.convertAddress import reverseAddress

class AddressView(APIView):
    def post(self, request):
        lat = request.data['lat']
        lng = request.data['lng']


        data = reverseAddress(lat, lng)

        if 'name' in request.data:
            data['property_name'] = request.data['name']
        if 'description' in request.data:
            data['property_description'] = request.data['description']

        serializer_class = AddressSerializer(data=data)

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
