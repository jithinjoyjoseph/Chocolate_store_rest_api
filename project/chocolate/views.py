from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

# Create your views here.
from .models import Chocolate
from .serializers import ChocoSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class ListChocolate(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='list.html'
    serializer_class = ChocoSerializer
    queryset = Chocolate.objects.all()

    def list(self,request):
        queryset=self.get_queryset()
        # serializer=ChocoSerializer(queryset,many=True)
        # return Response(serializer.data)
        return Response({'object_list':queryset})


class DetailChoco(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name='detail.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def get(self,request,*args,**kwargs):
        # queryset=Chocolate.objects.get(id=pk)
        queryset=self.get_object()
        #serializer=ChocoSerializer(queryset,many=False)
        # return Response({'object_list':queryset})
        # serializer=self.get_serializer(queryset)
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        authenticated = request.user.is_authenticated
        print('####',authenticated)
        if not authenticated:
            return redirect('list')

class ChocoCheckoutView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    template_name='checkout.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def get(self,request,*args,**kwargs):
        queryset=self.get_object()

        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        authenticated = request.user.is_authenticated
        print("###",authenticated)

        if not authenticated:
            return redirect('list')
        return Response({'object':queryset,'authenticated':authenticated})

        return Response({'object':queryset})



