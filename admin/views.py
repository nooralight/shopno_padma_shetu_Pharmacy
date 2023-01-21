from django.shortcuts import render, redirect
from account.models import User
from account.models import Seller,Company
from normal_user.models import OrderHistory_customer
from datetime import datetime
from company.models import OrderHistory_seller

# Create your views here.
def gotoAdmin(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':     
            users = User.objects.exclude(isAdmin='1')
            sellers  = Seller.objects.all()
            userCount = len(users)
            sellerCount = len(sellers)
            orders = OrderHistory_customer.objects.filter(verified="Yes")
            total_revenue = 0.00
            for order in orders:
                total_revenue += float(order.total)
            context = {"userCount": userCount,"sellerCount":sellerCount,"total_revenue":total_revenue}
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

def gotoSellers(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':     
            sellers = Seller.objects.all()

            context = {"sellers": sellers}
            return render(request, 'sellers.html',context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def gotoCompanies(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':     
            companies = Company.objects.all()

            context = {"companies": companies}
            return render(request, 'companies.html',context)
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

def deleteSeller(request, id):
    if 'user_id' in request.session:
        print(id)
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':
            seller = Seller.objects.get(id=id)
            seller.delete()
            return redirect('/admin/user_list/')
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')
def deleteCompany(request, id):
    if 'user_id' in request.session:
        print(id)
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='1':
            company = Company.objects.get(id=id)
            company.delete()
            return redirect('/admin/user_list/')
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def gotoTransections(request):
    orders = OrderHistory_customer.objects.all()
    datet = []
    for order in orders:
        datet.append(order.purchase_date)
    datet = list(set(datet))
    transections =[]
    
    for dt in datet:
        flag=0
        order_t = OrderHistory_customer.objects.filter(purchase_date = dt)
        for order in order_t:
            if order.delivered =="No":
                flag=1
                break
        transections.append({"dt":dt,"order_t":order_t,"flag":flag})
        print(flag)
    context = {"transections":transections}
    return render(request, "transections.html",context)

def makeDeliveredAdmin(request,dateTime):
    orders = OrderHistory_customer.objects.filter(purchase_date = dateTime)
    current_dateTime = datetime.now()
    orders.update(delivered = "Yes",delivered_dt = current_dateTime)
    return redirect('/admin/transactions/')

def gotoTransections_sellerToCompany(request):
    orders = OrderHistory_seller.objects.all()
    datet = []
    for order in orders:
        datet.append(order.order_dt)
    datet = list(set(datet))
    transections =[]
    
    for dt in datet:
        order_t = OrderHistory_seller.objects.filter(order_dt = dt)
        transections.append({"dt":dt,"order_t":order_t})
    context = {"transections":transections}
    return render(request, "sellerToCompany.html",context)