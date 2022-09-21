from django.urls import path
from .api import UserListAPIView, SignInAPI, UserRegisterAPIView

urlpatterns = [
    path('', UserListAPIView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),
    path('login/', SignInAPI.as_view()),
]