from django.shortcuts import render, redirect
from account.models import User,Seller
from seller.models import Shop_product
from cart.models import Cart
from .models import OrderHistory_customer

# Create your views here.
def gotoHome(request):
    return render(request, 'index.html')

def gotoVendors(request):
    shops= Seller.objects.all()
    print(type(shops))
    print(shops)
    context = {"shops": shops}
    return render(request,'vendors.html', context)


def gotoProducts(request):
    return render(request,'products.html')

def gotoShopProducts(request,id):
    shop = Seller.objects.get(id=int(id))
    products = Shop_product.objects.filter(shop_id = int(id))
    context = {"shop":shop,"products":products}
    return render(request,'shop_product_grid.html', context)

def gotoContact(request):
    return render(request, 'contact.html')

def gotoAbout(request):
    return render(request,'about.html')

def gotoProductDetails(request,id):
    product = Shop_product.objects.get(id=int(id))
    context={"product":product}
    return render(request,'product_details.html', context)




