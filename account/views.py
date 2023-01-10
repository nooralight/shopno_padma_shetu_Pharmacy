from django.shortcuts import render, redirect
from .models import User,Seller,Company

# Create your views here.
def gotoRegistration(request):
    return render(request, 'registration.html')

def gotoRegistration_Seller(request):
    return render(request, 'seller_registration.html')

def gotoRegistration_Company(request):
    return render(request, 'company_registration.html')

def gotoLogin(request):
    return render(request, 'login.html')

def gotoSellerLogin(request):
    return render(request,"seller_login.html")

def registerUser(request):
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    user = User.objects.create(first_name = f_name, last_name = l_name, email = email, phone= phone, password = password)
    user.save()
    return redirect('gotoLogin')

def registerSeller(request):
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    shop_name = request.POST.get("shop_name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    seller = Seller.objects.create(first_name = f_name, last_name = l_name,shop_name=shop_name, email = email, phone= phone, password = password)
    seller.save()
    return redirect('gotoLogin')


def login(request):
    input_email_or_mobile = request.GET.get("email_or_mobile")
    print(input_email_or_mobile)
    input_password = request.GET.get("password")

    try:
        registered_user = User.objects.get(email=input_email_or_mobile)
        
        if input_password == registered_user.password:
            print("login success")
            #return redirect('createyourshop')
            request.session['user_id'] = registered_user.id
            if registered_user.isAdmin == '1':
                response = redirect('/admin/')
                return response
            else:
                response = redirect('/')
                return response
        else:
            print("wrong password")
            return redirect('gotoLogin')
    except User.DoesNotExist:
        print("Email or Phone does not exist")
        return redirect('gotoLogin')
    #return redirect('createyourshop')

def login_shop(request):
    input_email_or_mobile = request.GET.get("email_or_mobile")
    print(input_email_or_mobile)
    input_password = request.GET.get("password")

    try:
        registered_shop = Seller.objects.get(email=input_email_or_mobile)
        
        if input_password == registered_shop.password:
            print("login success")
            #return redirect('createyourshop')
            request.session['user_id'] = registered_shop.id           
            response = redirect('/seller/')               
            return response
        else:
            print("wrong password")
            return redirect('seller-Login')
    except User.DoesNotExist:
        print("Email or Phone does not exist")
        return redirect('seller-Login')
    #return redirect('createyourshop')

def logout(request):
    request.session.flush()
    return redirect('/account/login/')
