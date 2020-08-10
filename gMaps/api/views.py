from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Address
from django.forms.models import model_to_dict
from .serializers import AddressSerializer
from rest_framework.parsers import MultiPartParser

class AddressViews()