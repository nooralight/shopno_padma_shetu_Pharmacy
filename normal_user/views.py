from django.shortcuts import render, redirect

# Create your views here.
def gotoHome(request):
    return render(request, 'home.html')