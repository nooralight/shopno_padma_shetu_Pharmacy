from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from account.models import User,Seller
from seller.models import Shop_product
from cart.models import Cart
from .models import OrderHistory_customer

# Create your views here.
def gotoHome(request):
    logged = False
    products = Shop_product.objects.order_by('-id')[:10:-1]
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            logged = True
            context = {"logged":logged,"products":products}
            return render(request, 'index_normal.html',context)
        else:
            return redirect('/account/logout/')
    else:
        context = {"logged":logged,"products":products}
        return render(request, 'index_normal.html',context)

def gotoVendors(request):
    logged = False
    shops= Seller.objects.all()
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            logged = True
            
            print(type(shops))
            print(shops)
            context = {"shops": shops,"logged":logged}
            return render(request,'vendors.html', context)
        else:
            return redirect('/account/logout/')
    else:
        context = {"shops": shops,"logged":logged}
        return render(request,'vendors.html', context)


def gotoProducts(request):
    logged = False
    products = Shop_product.objects.all()
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            logged = True
            context={"products":products,"logged":logged}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        context={"products":products,"logged":logged}
        return render(request,'products.html', context)

def gotoShopProducts(request,id):
    logged = False
    shop = Seller.objects.get(id=int(id))
    products = Shop_product.objects.filter(shop_id = int(id))
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            logged= True
            context = {"shop":shop,"products":products,"logged":logged}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        context = {"shop":shop,"products":products,"logged":logged}
        return render(request,'shop_product_grid.html', context)

def gotoContact(request):
    logged = False
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            logged= True
            return render(request, 'contact.html',{"logged":logged})
        else:
            return redirect('/account/logout/')
    else:
        return render(request, 'contact.html',{"logged":logged})

def gotoAbout(request):
    return render(request,'about.html')

def gotoOnlineDoctors(request):
    return render(request, "online_doctors.html")

def gotoProductDetails(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            product = Shop_product.objects.get(id=int(id))
            context={"product":product}
            return render(request,'product_details.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')



def category_OTC(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="OTC_Medicines")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Pres(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Prescription_Medicines")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Health(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Healthcare_Products")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Device(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Device_Equipment")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Baby(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Baby_Care")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Men(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Men_Products")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Woman(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Women_Product")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def category_Kid(request,id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            shop = Seller.objects.get(id=int(id))
            products = Shop_product.objects.filter(shop_id = int(id),category ="Kid_Product")
            context = {"shop":shop,"products":products}
            return render(request,'shop_product_grid.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def search_shop_product(request,id):
    search = request.POST.get("search")
    print(search)
    shop = Seller.objects.get(id = int(id))
    products = Shop_product.objects.filter(shop_id = int(id))
    names=[]
    generics =[]
    for product in products:
        names.append(product.name)
        generics.append(product.generic_name)
    if search in names:
        s_products = Shop_product.objects.filter(name = search)
    elif search in generics:
        s_products = Shop_product.objects.filter(generic_name = search)
    else:
        s_products = None
    context = {"shop":shop,"products":s_products}
    return render(request,'shop_product_grid.html', context)

def search_shop(request):
    search = request.POST.get("search")
    print(search)
    shops = Seller.objects.filter(shop_name= search)
    context = {"shops":shops}
    return render(request,'vendors.html', context)

def sorting(request,id):
    option = request.POST.get("sorting")
    if option=="byName":
        shop = Seller.objects.get(id=int(id))
        products = Shop_product.objects.filter(shop_id = int(id)).order_by('name')
        context = {"shop":shop,"products":products}
        return render(request,'shop_product_grid.html', context)
    else:
        shop = Seller.objects.get(id=int(id))
        products = Shop_product.objects.filter(shop_id = int(id)).order_by('price')
        context = {"shop":shop,"products":products}
        return render(request,'shop_product_grid.html', context)

def sorting_products(request):
    option = request.POST.get("sorting")
    if option=="byName":
        products = Shop_product.objects.order_by("name")
        context = {"products":products}
        return render(request,'products.html', context)
    else:
        products = Shop_product.objects.order_by("price")
        context = {"products":products}
        return render(request,'products.html', context)

def search_product(request):
    search = request.POST.get("search")
    print(search)
    products = Shop_product.objects.all()
    names=[]
    generics =[]
    for product in products:
        names.append(product.name)
        generics.append(product.generic_name)
    if search in names:
        s_products = Shop_product.objects.filter(name = search)
    elif search in generics:
        s_products = Shop_product.objects.filter(generic_name = search)
    else:
        s_products = None
    context = {"products":s_products}
    return render(request,'products.html', context)

def product_category_OTC(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="OTC_Medicines")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Pres(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Prescription_Medicines")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Health(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Healthcare_Products")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Device(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Device_Equipment")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Baby(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Baby_Care")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Men(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Men_Products")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Woman(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Women_Product")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def product_category_Kid(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        if user and user.isAdmin=='0':
            
            products = Shop_product.objects.filter(category ="Kid_Product")
            context = {"products":products}
            return render(request,'products.html', context)
        else:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')