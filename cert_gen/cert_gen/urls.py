"""cert_gen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from multiple import views as v1
from verification import views as v2
from django.contrib.auth import views as auth_views
from fetch import views as v3
from django.contrib.auth.views import LogoutView
# from home import views as v3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('',include('home.urls')),
    # path("", include('home.urls')),
    # path("multiple/", include('home.urls'))
    path('multiple/', v1.multiple, name='multiple'),
    path('verification/', v2.verification, name='verification'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('fetch/', v3.fetch, name="fetch"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
