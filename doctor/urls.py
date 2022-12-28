from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.gotoDoctorAdmin, name= 'drAdmin'),
    path('',views.gotoDoctors, name= 'gotoDoctors'),
]