from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Shop_product
from account.models import Seller,Company
from normal_user.models import OrderHistory_customer
from cart.models import Cart
from company.models import Company_product,OrderHistory_seller
from datetime import datetime
import string
import random

# Create your views here.

def gotoDashboard(request):
    if 'seller_id' in request.session:       
        shop = Seller.objects.get(id = request.session['seller_id'])
        context = {"shop_name":shop.shop_name}
        return render(request,"seller_dashboard_c.html",context)
    else:
        return redirect('/account/logout/')

def gotoAddProduct(request):
    if 'seller_id' in request.session:
        shop = Seller.objects.get(id = request.session['seller_id'])
        return render(request,"add_product_c.html",{"shop_name":shop.shop_name})
    else:
        return redirect('/account/logout/')    

def upload(request):
    if 'seller_id' in request.session:
        shop = Seller.objects.get(id=request.session['seller_id'])
        if request.method == 'POST':
            upload = request.FILES['upload']
            fss = FileSystemStorage()       
            name = request.POST.get("name")
            brand_name = request.POST.get("brand_name")
            quantity = request.POST.get("shop_name")
            price = request.POST.get("price")
            generic_name = request.POST.get("generic_name")
            quantity = request.POST.get("quantity")
            category = request.POST.get("category")
            sub_category = request.POST.get("sub_category")
            contradiction= request.POST.get("contradiction")
            pharmacology= request.POST.get("pharmacology")
            interaction= request.POST.get("interaction")
            side_effects= request.POST.get("side_effects")
            pregnancy= request.POST.get("pregnancy")
            warnings= request.POST.get("warnings")
            therapeutic= request.POST.get("therapeutic")
            storage_condition = request.POST.get("storage_condition")
            name_photo = str(shop.id)+"_"+name+upload.name[-5:]
            file = fss.save(name_photo, upload)
            file_url = fss.url(file)
            product = Shop_product.objects.create(name = name, brand_name = brand_name,quantity=quantity,generic_name= generic_name, price = price, category= category, product_photo = file_url,shop_id=shop.id,shop_name = shop.shop_name,sub_category=sub_category,
            contradiction=contradiction,pharmacology=pharmacology,interaction=interaction,side_effects=side_effects,pregnancy=pregnancy,warnings=warnings,
            therapeutic=therapeutic,storage_condition=storage_condition)
            product.save()
            return redirect('/seller/')
    else:
        return redirect('/account/logout/')

def gotoListProduct(request):
    if 'seller_id' in request.session:
        shop = Seller.objects.get(id = request.session['seller_id'])
        products = Shop_product.objects.filter(shop_id = int(request.session['seller_id']))
        context ={"products":products,"shop_name":shop.shop_name}
        return render(request, "product_list_c.html",context)
    else:
        return redirect('/account/logout/')

def gotoEdit_product_shop(request,id):
    product = Shop_product.objects.get(id=id)
    shop = Seller.objects.get(id = request.session['seller_id'])
    context = {"product":product,"shop_name":shop.shop_name,"action":"edit_product"}
    return render(request,"edit_product_shop.html",context)

def gotoEdit_Image_product_shop(request,id):
    product = Shop_product.objects.get(id=id)
    shop = Seller.objects.get(id = request.session['seller_id'])
    context = {"product":product,"shop_name":shop.shop_name,"action":"image"}
    return render(request,"edit_product_shop.html",context)

def edit_product_shop(request,id):
    product = Shop_product.objects.filter(id=id)
    name = request.POST.get("name")
    brand_name = request.POST.get("brand_name")
    quantity = request.POST.get("shop_name")
    price = request.POST.get("price")
    generic_name = request.POST.get("generic_name")
    quantity = request.POST.get("quantity")
    contradiction= request.POST.get("contradiction")
    pharmacology= request.POST.get("pharmacology")
    interaction= request.POST.get("interaction")
    side_effects= request.POST.get("side_effects")
    pregnancy= request.POST.get("pregnancy")
    warnings= request.POST.get("warnings")
    therapeutic= request.POST.get("therapeutic")
    storage_condition = request.POST.get("storage_condition")
    product.update(name = name, brand_name = brand_name,quantity=quantity,generic_name= generic_name, price = price,
            contradiction=contradiction,pharmacology=pharmacology,interaction=interaction,side_effects=side_effects,pregnancy=pregnancy,warnings=warnings,
            therapeutic=therapeutic,storage_condition=storage_condition)
    return redirect('/seller/product_list/')

def edit_product_image_shop(request,id):
    product = Shop_product.objects.filter(id=id)
    product_U = Shop_product.objects.get(id=id)
    shop = Seller.objects.get(id=request.session['seller_id'])
    name = product_U.name
    upload = request.FILES['upload']
    fss = FileSystemStorage()
    name_photo = str(shop.id)+"_"+name+upload.name[-5:]
    file = fss.save(name_photo, upload)
    file_url = fss.url(file)
    product.update( product_photo = file_url)
    return redirect('/seller/product_list/')
def editShop(request):
    if 'seller_id' in request.session:
        shop = Seller.objects.get(id=request.session['seller_id'])
        context = {"shop":shop,"shop_name":shop.shop_name}
        return render(request,"edit_shop.html",context)
    else:
        return redirect('/account/logout/')
def editing_shop(request):
    if 'seller_id' in request.session:
        shop = Seller.objects.filter(id=request.session['seller_id'])
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

def deleteProduct(request, id):
    if 'seller_id' in request.session:
        seller = Seller.objects.get(id = request.session['seller_id'])
        print(id)
        product = Shop_product.objects.get(id=id)
        product.delete()
        return redirect('/seller/product_list/')
    else:
        return redirect('/account/logout/')

def profilePic(request):
    if 'seller_id' in request.session:
        seller = Seller.objects.get(id = request.session['seller_id'])
        return render(request, "profilepic.html",{"shop_name":seller.shop_name})
    else:
        return redirect('/account/logout/')
def changePic(request):
    if 'seller_id' in request.session:
        shop = Seller.objects.filter(id=request.session['seller_id'])
        photo = request.FILES['photo']
        fss = FileSystemStorage()
        name_photo = str(shop[0].id)+"_"+shop[0].email+photo.name[-5:]
        file = fss.save(name_photo, photo)
        file_url = fss.url(file)
        shop.update(photo=file_url)
        return redirect('/seller/')
    else:
        return redirect('/account/logout/')

def gotoOrderList(request):
    if 'seller_id' in request.session:
        seller = Seller.objects.get(id = request.session['seller_id'])
        orders = OrderHistory_customer.objects.filter(shop_id = request.session['seller_id'])
        carts= Cart.objects.filter(shop_id=request.session['seller_id'],active="No")
        print(orders)
        context = {"orders":orders,"carts":carts,"shop_name":seller.shop_name}
        return render(request, "order_list.html", context)
    else:
        return redirect('/account/logout/')
def verify_order(request,id):
    if 'seller_id' in request.session:
        order = OrderHistory_customer.objects.filter(id = id)
        order.update(verified = "Yes")
        return redirect("/seller/order_list/")
    else:
        return redirect('/account/logout/')

def gotoCompanies(request):
    if 'seller_id' in request.session:
        companies = Company.objects.all()
        seller = Seller.objects.get(id = request.session['seller_id'])
        context = {"companies":companies,"shop_name":seller.shop_name}
        return render(request, "companies_seller.html",context)
    else:
        return redirect('/account/logout/')

def checkCompanyProducts(request, id):
    if 'seller_id' in request.session:
        seller = Seller.objects.get(id = request.session['seller_id'])
        company = Company.objects.get(id =id)
        products = Company_product.objects.filter(company_id= company.id)
        context = {"company":company,"products":products,"shop_name":seller.shop_name}
        return render(request, "company_product.html",context)
    else:
        return redirect('/account/logout/')

def making_order(request,company_id,id):
    if 'seller_id' in request.session:
        quantity = request.POST.get("purchase_quantity")
        seller = Seller.objects.get(id= request.session['seller_id'])
        product= Company_product.objects.get(id = id)
        current_dateTime = datetime.now()

        product_price = float(product.price)
        total_price = float(quantity)*product_price
        n = 7
        verified = ''.join(random.choices(string.ascii_letters, k=n))
        company = Company.objects.get(id = int(company_id))
        making_order = OrderHistory_seller.objects.create(company_id = company_id,shop_name = seller.shop_name,shop_email = seller.email,shop_phone = seller.phone,company_name= company.com_name,total_price = total_price,seller_id = seller.id,product_name = product.name,quantity = quantity,order_dt = current_dateTime,verified = verified)
        making_order.save()
        s_id = str(company_id)
        return redirect('/seller/company_products/'+s_id)
    else:
        return redirect('/account/logout/')

def gotoOrderHistory_comp(request):
    if 'seller_id' in request.session:
        seller = Seller.objects.get(id= request.session['seller_id'])
        order_history_seller = OrderHistory_seller.objects.filter(seller_id = seller.id)
        context= {"orderHistory":order_history_seller,"shop_name":seller.shop_name}
        return render(request,"purchase_history.html",context)
    else:
        return redirect('/account/logout/')

def product_category_company(request,id, category):
    if 'seller_id' in request.session:
        seller = Seller.objects.get(id= request.session['seller_id'])
        company = Company.objects.get(id =id)
        products = Company_product.objects.filter(company_id=id,category=category)
        context = {"company":company,"products":products,"shop_name":seller.shop_name}
        return render(request, "company_product.html",context)
    else:
        return redirect('/account/logout/')
