from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "password"]
        extra_kwargs = {"password":{"write_only": True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    

class UserLoginSerialzer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user 
        raise serializers.ValidationError("Invalid Email or Password!")