from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Address
from django.forms.models import model_to_dict
from .serializers import AddressSerializer
from rest_framework.parsers import MultiPartParser


class AddressViews(APIView):
    def post(self, request):
        serializer_class = AddressSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=200)
        return JsonResponse(serializer_class.errors, status=400)

    def get(self, request):
        address = Address.objects.all()
        serializer_class = AddressSerializer(address,many=True)
        return JsonResponse({'status': True, 'msg': 'Succesfully retrived categories', 'data': serializer_class.data},status=200)
