from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Shop_product
from account.models import Seller

# Create your views here.

def gotoDashboard(request):
    shop = Seller.objects.get(id = request.session['user_id'])
    context = {"shop_name":shop.shop_name}
    return render(request,"seller_dashboard.html",context)

def gotoAddProduct(request):
    return render(request,"add_product.html")

def upload(request):
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

def gotoListProduct(request):
    products = Shop_product.objects.filter(shop_id = int(request.session['user_id']))
    context ={"products":products}
    return render(request, "product_list.html",context)

def deleteProduct(request, id):
    print(id)
    product = Shop_product.objects.get(id=id)
    product.delete()
    return redirect('/seller/product_list/')