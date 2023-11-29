from django.contrib import admin
from django.urls import path, include
from multiple import views
from . import views
from verification import views

urlpatterns = [
    
    # path("", views.home, name="home")
    path("multiple/", views.multiple, name="multiple"),
    path("",views.upload, name="upload"),
    path("verification/",views.verification,name="verification")
]