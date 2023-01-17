from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Cart
from account.models import User,Seller
from seller.models import Shop_product
from datetime import datetime
from normal_user.models import OrderHistory_customer

def gotoCartPage(request):
    carts = Cart.objects.filter(customer_id=request.session['user_id'], active ="Yes")
    #carts = carts.filter(active= "Yes")
    total_price = 0.0
    prescr_needed= False
    for cart in carts:
        p =cart.total_price
        print(p)      
        total_price = total_price+float(p)
    
    for cart in carts:
        product_id = cart.product_id
        product = Shop_product.objects.get(id=product_id)
        if product.category=="Prescription Medicines":
            prescr_needed= True
            break

    print("Total Price= ",total_price)
    context = {"carts":carts,"sub_total":total_price,"total":total_price+30.0,"prescription_need":prescr_needed}
    return render(request,"cart_page.html",context)

def addingCart(request,id):
    product= Shop_product.objects.get(id=int(id))
    print("Product Sub-category= ", product.sub_category)
    if product.sub_category=="Tablet":
        if request.POST.get("purchase_quantity_pc") and int(request.POST.get("purchase_quantity_pc"))>0:
            quantity = request.POST.get("purchase_quantity_pc")
            b_quantity = str(quantity)+" pc"
            total_price = int(product.price)*int(quantity)
        elif request.POST.get("purchase_quantity_strip") and int(request.POST.get("purchase_quantity_strip"))>0:
            quantity = request.POST.get("purchase_quantity_strip")
            b_quantity = str(quantity)+" strip"
            total_price = int(product.price)*(int(quantity)*10)
        else:
            quantity = request.POST.get("purchase_quantity_box")
            b_quantity = str(quantity)+" box"
            total_price = int(product.price)*(int(quantity)*100)
    else:
        quantity = request.POST.get("purchase_quantity_pc")
        b_quantity = str(quantity)+" pc"
        total_price = int(product.price)*int(quantity)
    
    current_dateTime = datetime.now()
    cart = Cart.objects.create(product_id = int(product.id),shop_id = product.shop_id,product_name = product.name,quantity= b_quantity,total_price=total_price,order_date=current_dateTime,customer_id = int(request.session['user_id']))
    cart.save()
    return redirect("/")

def confirmingCart(request):
    carts = Cart.objects.filter(customer_id =request.session['user_id'],active = "Yes")
    prescr_needed= False
    current_dateTime = datetime.now()
    finished = True
    for cart in carts:
        product_id = cart.product_id
        product = Shop_product.objects.get(id=product_id)
        if product.category=="Prescription Medicines":
            # cart_up = Cart.objects.filter(id = cart.id)
            # cart_up.update(active="No")
            prescr_needed= True
            break
    if prescr_needed==True:
        presc = request.FILES['myfile']
        fs = FileSystemStorage()
        name_f = str(request.session['user_id'])+"_"+product.name+presc.name[-4:]
        filename = fs.save(name_f, presc)
        uploaded_file_url = fs.url(filename)
        carts.update(prescription = uploaded_file_url)
        for cart in carts:
            order_history = OrderHistory_customer.objects.create(purchase_date = current_dateTime,quantity = cart.quantity,product_name = cart.product_name,cart_id=cart.id,shop_id = cart.shop_id,customer_id=request.session['user_id'],total=cart.total_price,verified='No')
            order_history.save()
        carts.update(active="No")
    else:
        carts.update(active ="No")
        for cart in carts:
            order_history = OrderHistory_customer.objects.create(purchase_date = current_dateTime,quantity = cart.quantity,product_name = cart.product_name,cart_id=cart.id,shop_id = cart.shop_id,customer_id=request.session['user_id'],total=cart.total_price,verified='Yes')
            order_history.save()
            
    
    return redirect("/")

def deleteCartItem(request, id):
    print(id)
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect("/cart/")

def gotoOrders_customers(request):
    orders = OrderHistory_customer.objects.filter(customer_id= request.session['user_id'])
    context = {"orders":orders}
    return render(request, "order_history_customer.html", context)
