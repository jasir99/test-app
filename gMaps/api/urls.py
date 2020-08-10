from django.urls import path
from .models import Address
from api import views

urlpatterns = [
    path('address/', views.AddressView.as_view(), name='address'),
]