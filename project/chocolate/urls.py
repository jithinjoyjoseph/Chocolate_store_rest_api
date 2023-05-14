from django import views
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('chocolates/',views.ListChocolate.as_view(),name='list'),
    path('detail/<int:pk>',views.DetailChoco.as_view(),name='details'),
    path('checkout/<int:pk>/',views.ChocoCheckoutView.as_view(),name ='checkout'),

]