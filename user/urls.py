from django.urls import path
from user import views

urlpatterns = [
    path('user/register', views.RegisterAPI.as_view(), name='register'),
    path('user/login', views.LoginAPI.as_view(), name='login'),
    path('user/auth', views.UserAPI.as_view(), name='auth'),
    path('user/logout', views.LogOutAPI.as_view(), name='logout')
]