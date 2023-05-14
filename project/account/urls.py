from django import views
from django.contrib import admin
from django.urls import path
from .import views
from .views import RegisterView

urlpatterns = [
    path('register/',RegisterView.as_view(),name = 'register')

]