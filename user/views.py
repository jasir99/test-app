from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView

from .serializers import RegisterSerializer, UserSerializer

'''
  A class for registering users
'''


class RegisterAPI(APIView):
    def post(self, request, format='json'):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                data = {
                    'firstName': user.first_name,
                    'lastName': user.last_name,
                    'token': token.key,
                    'username': user.username,
                    'password': user.password
                }
                return JsonResponse({'status': True, 'msg': 'Succesfully created user', 'data': data}, status=200)
        return JsonResponse({'status': False, 'msg': 'Could not create user', 'data': {}}, status=200)


'''
  A class for login user
'''

class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user:
                token, create = Token.objects.get_or_create(user=user)
                data = {
                    'token': token.key,
                    'userId': user.pk,
                    'email': user.email,
                    'password': user.password
                }
                return JsonResponse({'status': True, 'msg': 'Succesfully logged in user', 'data': data}, status=200)
        return JsonResponse({'status': False, 'msg': 'Username or Password is incorect', 'data': {}}, status=200)


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user