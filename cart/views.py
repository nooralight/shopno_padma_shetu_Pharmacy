from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Cart
from account.models import User,Seller
from seller.models import Shop_product
from datetime import datetime

def gotoCartPage(request):
    carts = Cart.objects.filter(customer_id=request.session['user_id'])
    carts = carts.filter(active= "Yes")
    total_price = 0.0
    for cart in carts:
        p =cart.total_price
        print(p)
        
        total_price = total_price+float(p)
    print("Total Price= ",total_price)
    context = {"carts":carts,"sub_total":total_price,"total":total_price+30.0}
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

def confirmingCart(request,id):
    cart_user = Cart.objects.filter(customer_id =request.session['user_id'])
    
    presc = request.FILES['presc']
    fs = FileSystemStorage()
    name_f = str(request.session['user_id'])+"_"+presc.name[-4:]
    filename = fs.save(name_f, presc)
    uploaded_file_url = fs.url(filename)
    cart_user.update(prescription = uploaded_file_url)
    return render(request, 'core/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
