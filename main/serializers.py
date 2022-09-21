from rest_framework import serializers
from .models import Student, User
from django.contrib.auth import authenticate


# USER SERIALIZER 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# USER REGISTER SERIALIZER 

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['email', 'first_name', 'last_name', 'role', 'department','password']
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        

        user = User.objects.create_user(**validated_data)

        return user

# USER LOGIN SERIALER 
class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials, try again!!")
        


