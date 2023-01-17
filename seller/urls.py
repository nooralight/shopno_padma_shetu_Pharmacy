from django.urls import path
from . import views

urlpatterns=[
    path('' , views.gotoDashboard, name= 'seller-dashboard'),
    path('adding_product/' , views.gotoAddProduct, name= 'add-product'),
    path("upload", views.upload, name="upload"),
    path('product_list/' , views.gotoListProduct, name= 'list-product'),
    path('delete_product/<int:id>' , views.deleteProduct, name= 'delete-product'),
    path('edit_shop/',views.editShop, name="edit-shop"),
    path('editing',views.editing_shop, name='editing-shop'),
    path('profile_pic_change/',views.profilePic, name="edit-profile-pic"),
    path('changing_pic',views.changePic, name="change-pic"),
    path('order_list/', views.gotoOrderList, name='order-list-seller'),
    path('confirm_order_seller/<str:id>/', views.verify_order, name='verify-order-seller'),
]