from django.urls import path
from . import views

urlpatterns=[
    path('registration/',views.gotoRegistration, name= 'gotoRegistration'),
    path('registration_seller/',views.gotoRegistration_Seller, name= 'seller_registration_page'),
    path('registration_company/',views.gotoRegistration_Company, name= 'company_registration_page'),
    path('create_user' , views.registerUser, name= 'create-user'),
    path('create_seller' , views.registerSeller, name= 'create-seller'),
    path('create_company' , views.registerCompany, name= 'create-company'),
    path('login_user' , views.login, name= 'login-user'),
    path('login/' , views.gotoLogin, name= 'gotoLogin'),
    path('seller_login/' , views.gotoSellerLogin, name='seller-Login'),
    path('company_login/' , views.gotoCompanyLogin, name='company-Login'),
    path('login_seller' , views.login_shop, name= 'login-seller'),
    path('login_company' , views.login_company, name= 'login-company'),
    path('logout/' , views.logout, name= 'logout'),
]