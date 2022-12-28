from django.shortcuts import render

# Create your views here.

def gotoDoctorAdmin(request):
    return render(request,'doctorboard.html')

def gotoDoctors(request):
    return render(request,"doctors.html")