"""e_pharmacy URL Configuration

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
from django.urls import path,include
from django.conf import settings #add this
from django.conf.urls.static import static

urlpatterns = [
    path('account/', include('account.urls'), name = 'account'),
    path('',include('normal_user.urls'),name='normal-home'),
    path('admin/',include('admin.urls'),name='admin'),
    path('seller/',include('seller.urls'),name='seller'),
    path('cart/',include('cart.urls'),name='cart'),
    path('company/',include('company.urls'),name='company'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)