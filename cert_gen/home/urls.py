from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path("home/", views.home, name="home")
    # path("multiple", views.multiple, name="multiple")
]