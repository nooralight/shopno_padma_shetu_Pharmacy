from django.shortcuts import render, redirect
from account.models import User

# Create your views here.
def gotoAdmin(request):
    users = User.objects.exclude(isAdmin='1')
    userCount = len(users)
    context = {"userCount": userCount}
    return render(request,'admin_panel.html',context)

def gotoUsers(request):
    users = User.objects.exclude(isAdmin='1')

    context = {"users": users}
    return render(request, 'users.html',context)

def deleteUser(request, id):
    print(id)
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/admin/user_list/')
