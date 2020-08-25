from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView

from api.views import PropertyAddressView

from .serializers import RegisterSerializer, UserSerializer, LoginSerializer

'''
  A class for registering users
'''


class RegisterAPI(APIView):
    def post(self, request, format='json'):
        if 'is_staff' in request.data and request.data['is_staff'] or 'is_superuser' in request.data and request.data['is_superuser']:
            return JsonResponse({'status': False, 'msg': 'Unautorized request', 'data': {}}, status=200)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            token = Token.objects.create(user=user)
            data = {
                'token': token.key,
                'user': {
                    'userId': user.pk,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'email': user.email,
                    'address1': user.address1,
                    'address2': user.address2,
                    'phone_number': user.phone_number,
                },
            }
            return JsonResponse({'status': True, 'msg': 'Succesfully created user', 'data': data}, status=200)
        return JsonResponse({'status': False, 'msg': 'Could not create user', 'data': {}}, status=400)


'''
  A class for login user
'''

class LoginAPI(ObtainAuthToken):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        properties = serializer.validated_data['properties']
        if user:
            token, create = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'user': {
                    'userId': user.pk,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'email': user.email,
                    'address1': user.address1,
                    'address2': user.address2,
                    'phone_number': user.phone_number,
                    'properties': properties
                },
            }
            return JsonResponse({'status': True, 'msg': 'Succesfully logged in user', 'data': data}, status=200)
        return JsonResponse({'status': False, 'msg': 'Username or Password is incorect', 'data': {}}, status=401)


'''
  A class for logout user
'''

class LogOutAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except (AttributeError):
            pass

        return JsonResponse({'status': True, 'msg': 'Successfully logged out'}, status=200)


'''
  A class for retrieving authenticated user
'''

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user