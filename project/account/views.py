from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer


# Create your views here.

class RegisterView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'  #after creating register page  add it
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token,created = Token.objects.get_or_create(user = user)
            return Response(status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]


    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login = (request,user)