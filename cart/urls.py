from django.urls import path
from . import views

urlpatterns=[
    path("",views.gotoCartPage,name="goto-cart"),
    path("adding_cart/<str:id>/", views.addingCart,name="adding-cart"),
]