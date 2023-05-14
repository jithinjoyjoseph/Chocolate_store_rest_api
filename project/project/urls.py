"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chocolate',include("chocolate.urls")),
    path('account',include("account.urls")),
    path('token/',obtain_auth_token),                       #login,register ellathe direct token vech acess cheyenethan eth
    path('jwt/token/',TokenObtainPairView.as_view()),
    path('jwt/token/refresh/',TokenRefreshView.as_view()),


]


# adding jwt or "pip install djangorestframework-simplejwt"
#'token/' vere olla link eduth postmanil poi paste cheyenem
#enit userauth create cheyenem
#createsuperuser cheyuka,user and password kodukkuka
#postmanil poit ee user and password koduthal namuke token generate avum
