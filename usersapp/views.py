from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerialzer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationAPIView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data 
        serializer.save()
        return Response("User created.", status=status.HTTP_200_OK)
    

class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerialzer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data 
        # Generate token for user if user exist
        if User.objects.filter(email=serializer.data["email"]).exists():
            user = User.objects.get(email=serializer.data["email"])
            refresh_token = RefreshToken.for_user(user)
            refreshToken = str(refresh_token)
            accessToken = str(refresh_token.access_token)
            return Response({"message":"User created.", "tokens":{"refresh": refreshToken, "access":accessToken}}, status=status.HTTP_200_OK)
        return Response("User not found", status=status.HTTP_400_BAD_REQUEST)

        