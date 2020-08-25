from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView

from .serializers import RegisterSerializer, UserSerializer

'''
  A class for registering users
'''


class RegisterAPI(APIView):
    def post(self, request, format='json'):
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
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
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
                    'properties': user.properties,
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