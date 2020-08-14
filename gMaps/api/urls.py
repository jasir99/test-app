from django.urls import path
from .models import PropertyAddress,PropertyImage
from api import views

urlpatterns = [
    path('address/', views.AddressView.as_view(), name='address'),
    path('address/<str:latLong>', views.AddressView.as_view(), name='address1'),
]