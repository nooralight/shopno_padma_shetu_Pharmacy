from django.urls import path
from . import views

urlpatterns=[
    path("",views.gotoCartPage,name="goto-cart"),
    path("adding_cart/<str:id>/", views.addingCart,name="adding-cart"),
    path("delete_cart/<str:id>/", views.deleteCartItem,name="delete-cart"),
    path("confirming_cart", views.confirmingCart, name="confirm-cart"),
    path("order_history/",views.gotoOrders_customers,name="goto-Orders"),
]