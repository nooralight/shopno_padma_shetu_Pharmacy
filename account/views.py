from django.shortcuts import render, redirect
from .models import User,Seller,Company

# Create your views here.
def gotoRegistration(request):
    return render(request, 'registration.html')

def gotoLogin(request):
    return render(request, 'login.html')


def registerUser(request):
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    user = User.objects.create(first_name = f_name, last_name = l_name, email = email, phone= phone, password = password)
    user.save()
    return redirect('gotoLogin')