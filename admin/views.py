from django.shortcuts import render, redirect
from account.models import User

# Create your views here.
def gotoAdmin(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':     
            users = User.objects.exclude(isAdmin='1')
            userCount = len(users)
            context = {"userCount": userCount}
            return render(request,'admin_panel.html',context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def gotoUsers(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':     
            users = User.objects.exclude(isAdmin='1')

            context = {"users": users}
            return render(request, 'users.html',context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def deleteUser(request, id):
    if 'user_id' in request.session:
        print(id)
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':
            user_d = User.objects.get(id=id)
            user_d.delete()
            return redirect('/admin/user_list/')
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')
