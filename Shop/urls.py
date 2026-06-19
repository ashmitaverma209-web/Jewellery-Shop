"""
URL configuration for cse3d project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='home'),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('pricing/', views.pricing),
    path("login/", views.login),
    path("signup/", views.signup),
    path('new-collection/', views.collection),
    path('shop-online/', views.shop),
    path('collaboration/', views.collaboration),
    path('about/', views.about),
]



