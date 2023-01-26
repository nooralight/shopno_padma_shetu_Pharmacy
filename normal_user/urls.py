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
    path('shop_products/category/OTC/<int:id>',views.category_OTC, name= 'shop-category-otc'),
    path('shop_products/category/Pres/<int:id>',views.category_Pres, name= 'shop-category-pres'),
    path('shop_products/category/Health/<int:id>',views.category_Health, name= 'shop-category-health'),
    path('shop_products/category/Device/<int:id>',views.category_Device, name= 'shop-category-device'),
    path('shop_products/category/Baby/<int:id>',views.category_Baby, name= 'shop-category-baby'),
    path('shop_products/category/Men/<int:id>',views.category_Men, name= 'shop-category-men'),
    path('shop_products/category/Woman/<int:id>',views.category_Woman, name= 'shop-category-women'),
    path('shop_products/category/Kid/<int:id>',views.category_Kid, name= 'shop-category-kid'),
    path('search_product_shop/<int:id>',views.search_shop_product,name = 'search-shop-product'),
    path('search_shops/',views.search_shop,name = 'search-shop'),
    path('search_products/',views.search_product,name = 'search-products'),
    path('sorting/<int:id>/',views.sorting,name = 'sorting'),
    path('sorting_products/',views.sorting_products,name = 'products-sort'),

    path('product/category/OTC/',views.product_category_OTC, name= 'product-category-otc'),
    path('product/category/Pres/',views.product_category_Pres, name= 'product-category-pres'),
    path('product/category/Health/',views.product_category_Health, name= 'product-category-health'),
    path('product/category/Device/',views.product_category_Device, name= 'product-category-device'),
    path('product/category/Baby/',views.product_category_Baby, name= 'product-category-baby'),
    path('product/category/Men/',views.product_category_Men, name= 'product-category-men'),
    path('product/category/Woman/',views.product_category_Woman, name= 'product-category-women'),
    path('product/category/Kid/',views.product_category_Kid, name= 'product-category-kid'),
    path('online_doctors/',views.gotoOnlineDoctors,name="gotoDoctors"),

]