import random

from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from . import serializers
from . import models
from backend import settings

def generate_random_otp(length=8):
        otp = "".join([str(random.randint(0,9)) for _ in range(length)])
        return otp


class MyTokenView(TokenObtainPairView):
        serializer_class = serializers.MyTokenSerializer


class RegistrationView(generics.CreateAPIView):
        queryset = models.User.objects.all()
        permission_classes = [AllowAny]
        serializer_class = serializers.RegistrationSerializer



class PasswordResetView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        email = self.kwargs["email"]
        user = models.User.objects.filter(email=email).first()
        

        if user is not None:
            print(user)
            uuidb64 = user.pk
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)
            user.refresh_token = refresh_token
            user.otp = generate_random_otp()
            user.save()

            link = f"http://localhost:5173/new_password/?otp={user.otp}&uuidb64={uuidb64}&=refresh_token{refresh_token}"
            print(link)

            context = {"link": link, "username": user.username}

            subject = "Password reset email"
            text_body = render_to_string("password_reset.txt", context)
            html_body = render_to_string("password_reset.html", context)

            message = EmailMultiAlternatives(
                subject=subject,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],
                body=text_body,
            )

            message.attach_alternative(html_body, "text/html")
            message.send()
        return user


class PasswordChangeView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        otp = request.data["otp"]
        uuidb64 = request.data["uuidb64"]
        password = request.data["password"]

        user = models.User.objects.get(id=uuidb64, otp=otp)

        if user:
            user.set_password(password)
            user.save()

            return Response(
                {"message": "Password Changed Successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND
            )


