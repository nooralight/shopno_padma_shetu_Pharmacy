from django.urls import path
from . import views

urlpatterns=[
    path("",views.gotoDashboard,name="company-dashboard"),
    path("adding_product_company/" , views.gotoAddProduct, name= 'add-product-company'),
    path("upload", views.upload, name="upload-company"),
    path('product_list_company/' , views.gotoListProduct, name= 'list-product-company'),
    path('delete_product_company/<int:id>' , views.deleteProduct, name= 'delete-product-company'),
    path('edit_company/',views.editCompany, name="edit-company"),
    path('editing_company',views.editing_company, name='editing-company'),
    path('order_lists/',views.gotoOrderList_sellers,name="order-lists-sellers"),
    path('make_delivered/<int:id>/',views.make_delivered,name="make-delivered"),
]