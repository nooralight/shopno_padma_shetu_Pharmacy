from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Shop_product
from account.models import Seller
from normal_user.models import OrderHistory_customer
from cart.models import Cart

# Create your views here.

def gotoDashboard(request):
    print(request.session)
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:   
                shop = Seller.objects.get(id = request.session['user_id'])
                context = {"shop_name":shop.shop_name}
                return render(request,"seller_dashboard_c.html",context)
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def gotoAddProduct(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                return render(request,"add_product_c.html")
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')    

def upload(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                shop = Seller.objects.get(id=request.session['user_id'])
                if request.method == 'POST':
                    upload = request.FILES['upload']
                    fss = FileSystemStorage()       
                    name = request.POST.get("name")
                    brand_name = request.POST.get("brand_name")
                    quantity = request.POST.get("shop_name")
                    price = request.POST.get("price")
                    quantity = request.POST.get("quantity")
                    category = request.POST.get("category")
                    sub_category = request.POST.get("sub_category")
                    name_photo = str(shop.id)+"_"+name+upload.name[-4:]
                    file = fss.save(name_photo, upload)
                    file_url = fss.url(file)
                    product = Shop_product.objects.create(name = name, brand_name = brand_name,quantity=quantity, price = price, category= category, product_photo = file_url,shop_id=shop.id,sub_category=sub_category)
                    product.save()
                    return redirect('/seller/')
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def gotoListProduct(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                products = Shop_product.objects.filter(shop_id = int(request.session['user_id']))
                context ={"products":products}
                return render(request, "product_list_c.html",context)
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')
def editShop(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                shop = Seller.objects.get(id=request.session['user_id'])
                context = {"shop":shop}
                return render(request,"edit_shop.html",context)
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')
def editing_shop(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                shop = Seller.objects.filter(id=request.session['user_id'])
                f_name = request.POST.get("f_name")
                l_name = request.POST.get("l_name")
                shop_name = request.POST.get("shop_name")
                email = request.POST.get("email")
                phone = request.POST.get("phone")
                address = request.POST.get("address")
                # if request.FILES['photo'] is not None:
                #     photo = request.FILES['photo']
                #     fss = FileSystemStorage()
                #     name_photo = str(shop[0].id)+"_"+shop[0].email+photo.name[-4:]
                #     file = fss.save(name_photo, photo)
                #     file_url = fss.url(file)
                #     shop.update(first_name = f_name,last_name = l_name,photo=file_url,shop_name = shop_name,email=email,phone=phone,address =address)
                # else:
                shop.update(first_name = f_name,last_name = l_name,shop_name = shop_name,email=email,phone=phone,address =address)
                #shop.save()
                return redirect('/seller/')
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def deleteProduct(request, id):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                print(id)
                product = Shop_product.objects.get(id=id)
                product.delete()
                return redirect('/seller/product_list/')
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def profilePic(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                return render(request, "profilepic.html")
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')
def changePic(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                shop = Seller.objects.filter(id=request.session['user_id'])
                photo = request.FILES['photo']
                fss = FileSystemStorage()
                name_photo = str(shop[0].id)+"_"+shop[0].email+photo.name[-4:]
                file = fss.save(name_photo, photo)
                file_url = fss.url(file)
                shop.update(photo=file_url)
                return redirect('/seller/')
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')

def gotoOrderList(request):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                orders = OrderHistory_customer.objects.filter(shop_id = request.session['user_id'])
                carts= Cart.objects.filter(shop_id=request.session['user_id'],active="No")
                print(orders)
                context = {"orders":orders,"carts":carts}
                return render(request, "order_list.html", context)
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')
def verify_order(request,id):
    if 'user_id' in request.session:
        try:
            seller = Seller.objects.get(id = request.session['user_id'])
            if seller and seller.shop_name:
                order = OrderHistory_customer.objects.filter(id = id)
                order.update(verified = "Yes")
                return redirect("/seller/order_list/")
            else:
                return redirect('/account/logout/')
        except:
            return redirect('/account/logout/')
    else:
        return redirect('/account/login/')