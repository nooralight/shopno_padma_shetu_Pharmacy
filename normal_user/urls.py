from django.urls import path
from . import views

urlpatterns=[
    path('',views.gotoHome, name= 'gotoHome'),
    path('vendors/',views.gotoVendors, name= 'gotoVendor'),
    path('about/',views.gotoAbout, name= 'gotoAbout'),
    path('contact/',views.gotoContact, name= 'gotoContact'),
    path('products/',views.gotoProducts, name= 'gotoProducts'),
    path('shop_products/<int:id>',views.gotoShopProducts,name = 'gotoShop'),
    path('product_details/<int:id>',views.gotoProductDetails, name= 'productDetails'),

]