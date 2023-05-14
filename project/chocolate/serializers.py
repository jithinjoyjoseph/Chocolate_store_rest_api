from rest_framework import serializers
from .models import  Chocolate,Carts


class ChocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields =('id','category','description','price','image_url','choco_available')


class CartSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    product=serializers.CharField(read_only=True)
    user= serializers.CharField(read_only=True)