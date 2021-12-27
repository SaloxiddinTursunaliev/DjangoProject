from ..models import *
from .accountsserializers import *

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import authenticate

from django.utils import timezone


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:

            # from django.contrib.auth.models import User
            # u = User.objects.get(username='john')
            # u.set_password('new password')
            # u.save()

            # user.username = request.data.get("first_name")
            # # user.save(update_fields=['username'])

            # user.last_login = timezone.now()
            # # user.save(update_fields=['last_login'])

            # user.is_staff = request.data.get("is_staff")
            # # user.save(update_fields=['is_staff'])

            # user.is_superuser = request.data.get("is_superuser")
            # # user.save(update_fields=['is_superuser'])

            # user.save()

            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_active": user.is_active,
                    "last_login": user.last_login,
                    "pk": user.pk,
                    "password encrypted": user.password,
                    "token": user.auth_token.key
                },
            )

        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    #queryset2 = Poll.objects.select_related()
    serializer_class = UsersListSerializer
