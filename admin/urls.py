from django.urls import path
from . import views

urlpatterns=[
    path('',views.gotoAdmin, name= 'gotoAdmin'),
    path('user_list/',views.gotoUsers, name= 'gotoUsers'),
    path('seller_list/',views.gotoSellers, name= 'gotoSellers'),
    path('delete_user/<str:id>/', views.deleteUser, name="delete-user"),
    path('delete_seller/<str:id>/', views.deleteSeller, name="delete-seller"),
    path('transections/',views.gotoTransections, name= 'transections'),
]