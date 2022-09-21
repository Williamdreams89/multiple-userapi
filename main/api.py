from rest_framework import generics
from rest_framework.response import Response
from main.models import User
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserSerializer
from knox.models import AuthToken


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("id")



class UserRegisterAPIView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1],
            "message": "User Registered Successfully!!"
        })

class SignInAPI(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

