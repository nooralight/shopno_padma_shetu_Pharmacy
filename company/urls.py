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
    path('edit_company_logo/',views.editCompany_logo, name="edit-company-logo"),
    path('editing_company_logo',views.editing_company_logo, name='editing-company-logo'),
    path('order_lists/',views.gotoOrderList_sellers,name="order-lists-sellers"),
    path('make_delivered/<int:id>/',views.make_delivered,name="make-delivered"),

    path('edit_company_product/<int:id>/' , views.gotoEdit_product_company, name= 'editProduct-company'),
    path('edit_company_product_image/<int:id>/' , views.gotoEdit_Image_product_company, name= 'editProduct-company-image'),
    path('editing_company_product/<int:id>/' , views.edit_product_company, name= 'edit-company-product'),
    path('editing_company_product_image/<int:id>/' , views.edit_product_image_company, name= 'edit-company-product-image'),
]