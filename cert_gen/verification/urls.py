from django.contrib import admin
from django.urls import path, include
from verification import views
# from . import views

urlpatterns = [
    
    # path("", views.home, name="home")
    path("verification/", views.verification, name="verification"),
    # path("",views.upload, name="upload")
]