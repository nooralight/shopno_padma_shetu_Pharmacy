from django.urls import path
from . import views

urlpatterns=[
    path('' , views.gotoDashboard, name= 'seller-dashboard'),
    path('adding_product/' , views.gotoAddProduct, name= 'add-product'),
    path("upload", views.upload, name="upload"),
    path('product_list/' , views.gotoListProduct, name= 'list-product'),
    path('delete_product/<int:id>' , views.deleteProduct, name= 'delete-product'),
]