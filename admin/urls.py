from django.urls import path
from . import views

urlpatterns=[
    path('',views.gotoAdmin, name= 'gotoAdmin'),
    path('user_list/',views.gotoUsers, name= 'gotoUsers'),
    path('seller_list/',views.gotoSellers, name= 'gotoSellers'),
    path('company_list_admin/',views.gotoCompanies, name= 'gotoCompanies-admin'),
    path('delete_user/<str:id>/', views.deleteUser, name="delete-user"),
    path('delete_seller/<str:id>/', views.deleteSeller, name="delete-seller"),
    path('delete_company/<str:id>/', views.deleteSeller, name="delete-company"),
    path('transactions/',views.gotoTransections, name= 'transections'),
    path('make_delivered_Orders/<str:dateTime>/',views.makeDeliveredAdmin,name="make-delivered-admin"),
    path('transactions_seller_to_company/',views.gotoTransections_sellerToCompany, name= 'transections-sellerCompany'),
]