from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
# from .permissions import IsAdminUserReadOnly,IsOwneronly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle

# Create your views here.

@ api_view(['POST'])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message":"you are logged out"}, status=status.HTTP_200_OK)


@api_view(["POST", ])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Account has been created'
            data['username'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

        else:
            data = serializer.errors
        return Response(data)