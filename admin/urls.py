from django.urls import path
from . import views

urlpatterns=[
    path('',views.gotoAdmin, name= 'gotoAdmin'),
]