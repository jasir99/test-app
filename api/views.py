from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework import viewsets

from .models import PropertyAddress, PropertyImage
from .serializers import PropertyAddressSerializer, PropertyImageSerializer, PropertyAddressSerializerWithImages

from .utils.convertAddress import reverseAddress


class PropertyAddressView(viewsets.ViewSet):

    def get_queryset(self):
        latLong = self.request.query_params.get('latLng')
        if latLong is None:
            queryset = PropertyAddress.objects.all()
        else:
            queryset = PropertyAddress.objects.filter(latLong=latLong)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PropertyAddressSerializer(queryset, many=True)
        return JsonResponse({'status': True, 'msg': 'Succesfully retrived categories', 'data': serializer.data})

    def retrieve(self, request, pk=None):
        queryset = PropertyAddress.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = PropertyAddressSerializerWithImages(address)

        return JsonResponse({'status': True, 'data': serializer.data})

    def create(self, request):
        lat = request.data['lat']
        lng = request.data['lng']
        autocomplete_address = request.data['address']
        data = reverseAddress(lat, lng, autocomplete_address)

        if 'description' in request.data:
            data['property_description'] = request.data['description']

        address_serializer_class = PropertyAddressSerializer(data=data)

        if address_serializer_class.is_valid():
            address_serializer_class.save()
            return JsonResponse(address_serializer_class.data, status=200)
        return JsonResponse(address_serializer_class.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = PropertyAddress.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = PropertyAddressSerializer(address)
        address.delete()
        return JsonResponse({'delete': True, 'data': serializer.data})


class PropertyImageView(viewsets.ViewSet):

    def list(self, request):
        queryset = PropertyImage.objects.all()
        image_serializer_class = PropertyImageSerializer(queryset, many=True)
        return JsonResponse({'status': True, 'msg': 'Succesfully retrived categories', 'data': image_serializer_class.data})

    def retrieve(self, request, pk=None):
        queryset = PropertyImage.objects.filter(propertyAddress=pk)
        image_serializer_class = PropertyImageSerializer(queryset, many=True)
        return JsonResponse({'status': True, 'data': image_serializer_class.data})

    def create(self, request):
        image_serializer_class = PropertyImageSerializer(data=request.data)
        if image_serializer_class.is_valid():
            image_serializer_class.save()
            return JsonResponse({'status': True, 'data': image_serializer_class.data}, status=200)
        return JsonResponse({'status': False, 'data': image_serializer_class.errors}, status=400)

    def destroy(self, request, pk=None):
        queryset = PropertyImage.objects.all()
        image = get_object_or_404(queryset, pk=pk)
        serializer = PropertyImageSerializer(image)
        image.delete()
        return JsonResponse({'delete': True, 'data': serializer.data})