from django.urls import path
from . import views

urlpatterns=[
    path('',views.gotoAdmin, name= 'gotoAdmin'),
    path('user_list/',views.gotoUsers, name= 'gotoUsers'),
    path('delete_user/<str:id>/', views.deleteUser, name="delete-user"),
]