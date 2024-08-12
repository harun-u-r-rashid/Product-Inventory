from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path("user/login/", views.MyTokenView.as_view(), name="user_token"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("user/register", views.RegistrationView.as_view(), name="register"),
    path("user/password/reset/<email>/", views.PasswordResetView.as_view(), name="reset"),
    path("user/password/change/", views.PasswordChangeView.as_view(), name="change"),

]
