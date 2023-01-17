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
    path('product/category/OTC/<int:id>',views.category_OTC, name= 'shop-category-otc'),
    path('product/category/Pres/<int:id>',views.category_Pres, name= 'shop-category-pres'),
    path('product/category/Health/<int:id>',views.category_Health, name= 'shop-category-health'),
    path('product/category/Device/<int:id>',views.category_Device, name= 'shop-category-device'),
    path('product/category/Baby/<int:id>',views.category_Baby, name= 'shop-category-baby'),
    path('product/category/Men/<int:id>',views.category_Men, name= 'shop-category-men'),
    path('product/category/Woman/<int:id>',views.category_Woman, name= 'shop-category-women'),
    path('product/category/Kid/<int:id>',views.category_Kid, name= 'shop-category-kid'),

]