from django.urls import path
from . import views

urlpatterns=[
    path('registration/',views.gotoRegistration, name= 'gotoRegistration'),
    path('create_user' , views.registerUser, name= 'create-user'),
    path('login_user' , views.login, name= 'login-user'),
    path('login/' , views.gotoLogin, name= 'gotoLogin'),
    path('logout/' , views.logout, name= 'logout'),
]