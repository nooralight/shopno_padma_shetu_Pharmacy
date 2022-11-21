from django.shortcuts import render

# Create your views here.
def gotoRegistration(request):
    return render(request, 'registration.html')

def gotoLogin(request):
    return render(request, 'login.html')