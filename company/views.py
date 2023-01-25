from django.shortcuts import render, redirect
from account.models import Company
from django.core.files.storage import FileSystemStorage
from .models import Company_product,OrderHistory_seller
from datetime import datetime

# Create your views here.
def gotoDashboard(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id = request.session['company_id'])
        return render(request, "dashboard.html",{"com_name":company.com_name})
    else:
        return redirect('/account/logout/')   

def gotoAddProduct(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id = request.session['company_id'])
        return render(request,"add_product_company.html",{"com_name":company.com_name})
    else:
        return redirect('/account/logout/')    

def upload(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id=request.session['company_id'])
        if request.method == 'POST':
            upload = request.FILES['upload']
            fss = FileSystemStorage()       
            name = request.POST.get("name")
            price = request.POST.get("price")
            category = request.POST.get("category")
            sub_category = request.POST.get("sub_category")
            generic_name = request.POST.get("generic_name")
            contradiction= request.POST.get("contradiction")
            pharmacology= request.POST.get("pharmacology")
            interaction= request.POST.get("interaction")
            side_effects= request.POST.get("side_effects")
            pregnancy= request.POST.get("pregnancy")
            warnings= request.POST.get("warnings")
            therapeutic= request.POST.get("therapeutic")
            storage_condition = request.POST.get("storage_condition") 
            name_photo = str(company.id)+"_company_product_"+name+upload.name[-4:]
            file = fss.save(name_photo, upload)
            file_url = fss.url(file)
            product = Company_product.objects.create(name = name, price = price, category= category, product_photo = file_url,company_id=company.id,company_name = company.com_name,sub_category=sub_category,
            generic_name=generic_name,contradiction=contradiction,pharmacology=pharmacology,interaction=interaction,side_effects=side_effects,pregnancy=pregnancy,warnings=warnings,
            therapeutic=therapeutic,storage_condition=storage_condition)
            product.save()
            return redirect('/company/')
    else:
        return redirect('/account/logout/')

def gotoListProduct(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id = request.session['company_id'])
        products = Company_product.objects.filter(company_id = int(request.session['company_id']))
        context ={"products":products,"com_name":company.com_name}
        return render(request, "product_list_company.html",context)
    else:
        return redirect('/account/logout/')

def deleteProduct(request, id):
    if 'company_id' in request.session:
        company = Company.objects.get(id = request.session['company_id'])
        print(id)
        product = Company_product.objects.get(id=id)
        product.delete()
        return redirect('/company/product_list/')
    else:
        return redirect('/account/logout/')

def editCompany(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id=request.session['company_id'])
        context = {"company":company,"com_name":company.com_name,"action":"edit_company"}
        return render(request,"edit_company.html",context)
    else:
        return redirect('/account/logout/')

def editCompany_logo(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id=request.session['company_id'])
        context = {"company":company,"com_name":company.com_name,"action":"logo"}
        return render(request,"edit_company.html",context)
    else:
        return redirect('/account/logout/')

def editing_company(request):
    if 'company_id' in request.session:
        company = Company.objects.filter(id=request.session['company_id'])
        com_name = request.POST.get("com_name")
        admin_name = request.POST.get("admin_name")
        com_email = request.POST.get("com_email")
        com_phone = request.POST.get("com_phone")
        tin_no = request.POST.get("tin_no")
        com_address = request.POST.get("com_address")
        com_reg_no = request.POST.get("com_reg_no")
        company.update(com_name=com_name,admin_name =admin_name,com_email = com_email,com_phone = com_phone,tin_no=tin_no,com_address=com_address,com_reg_no= com_reg_no)
        #shop.save()
        return redirect('/company/')
    else:
        return redirect('/account/logout/')

def editing_company_logo(request):
    if 'company_id' in request.session:
        company = Company.objects.filter(id=request.session['company_id'])
        company_U = Company.objects.get(id=request.session['company_id'])
        upload = request.FILES['photo']
        fss = FileSystemStorage()
        name_photo = str(company_U.id)+"_com_logo_"+company_U.com_name+upload.name[-5:]
        file = fss.save(name_photo, upload)
        file_url = fss.url(file)
        company.update(company_logo = file_url)
        #shop.save()
        return redirect('/company/')
    else:
        return redirect('/account/logout/')

def gotoOrderList_sellers(request):
    if 'company_id' in request.session:
        company = Company.objects.get(id = request.session['company_id'])
        orderHistory = OrderHistory_seller.objects.filter(company_id= company.id)
        context = {"orderHistory":orderHistory,"com_name":company.com_name}
        return render(request,"order_list_ofCompany.html",context)
    else:
        return redirect('/account/logout/')

def make_delivered(request, id):
    if 'company_id' in request.session:
        order = OrderHistory_seller.objects.filter(id = id)
        current_dateTime = datetime.now()
        order.update(delivered = "Yes",delivered_dt = current_dateTime)
        return redirect('/company/order_lists/')
    else:
        return redirect('/account/logout/')