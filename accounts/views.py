from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer


class ProfileCreateView(generics.CreateAPIView):
    model = get_user_model()
    fields = ['username', 'email', 'password']
    authentication_classes = [TokenAuthentication]
    permission_classes = []


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    fields = ['username', 'email', 'first_name', 'last_name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ProfileView(generics.RetrieveAPIView):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    fields = ['username', 'email', 'first_name', 'last_name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return self.model.objects.filter(pk=self.request.user.pk)
