from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Cart
from account.models import User,Seller

def gotoCartPage(request):
    user = User.objects.get(id = request.session['user_id'])
    cart_user = Cart.objects.filter(customer_id =user.id)
    context ={"cart_details":cart_user}
    return redirect(request, "cart_page.html",context)

def confirmingCart(request,id):
    cart_user = Cart.objects.filter(customer_id =request.session['user_id'])
    
    presc = request.FILES['presc']
    fs = FileSystemStorage()
    name_f = str(request.session['user_id'])+"_"+presc.name[-4:]
    filename = fs.save(name_f, presc)
    uploaded_file_url = fs.url(filename)
    cart_user.update(prescription = uploaded_file_url)
    return render(request, 'core/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
