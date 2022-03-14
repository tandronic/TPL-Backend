from django.contrib import admin
from django.urls import path, include

from user.views import RegisterAPIView, ActivateAPIView, ChangePasswordAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/', ActivateAPIView.as_view()),
    path('change-password/', ChangePasswordAPIView.as_view()),
]
