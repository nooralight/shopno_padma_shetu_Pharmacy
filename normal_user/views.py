from django.shortcuts import render, redirect

# Create your views here.
def gotoHome(request):
    return render(request, 'index.html')

def gotoVendors(request):
    return render(request,'vendors.html')


def gotoProducts(request):
    return render(request,'products.html')

def gotoShopProducts(request):
    return render(request,'shop_product_grid.html')

def gotoContact(request):
    return render(request, 'contact.html')

def gotoAbout(request):
    return render(request,'about.html')

def gotoProductDetails(request):
    return render(request,'product_details.html')
