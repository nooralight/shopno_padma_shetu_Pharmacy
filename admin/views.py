from django.shortcuts import render, redirect

# Create your views here.
def gotoAdmin(request):
    return render(request,'admin_panel.html')
