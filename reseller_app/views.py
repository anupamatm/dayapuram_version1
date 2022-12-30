from django.shortcuts import render,redirect

from reseller_app.models import Product, Reseller
from django.http import JsonResponse

# Create your views here.

def reseller_home(request):
    seller=Reseller.objects.get(id=request.session['s_id'])
    return render(request,'reseller_app/reseller_home.html',{'seller_details':seller})

def product_catalogue(request):
    product_list=Product.objects.filter(seller_id=request.session['s_id']) 
    return render(request,'reseller_app/catalogue.html',{'products':product_list})

def add_product(request):
    msg=""
    if request.method == 'POST':
            pr_name = request.POST['p_name']            
            pr_number = request.POST['p_no']
            pr_description = request.POST['p_description']
            pr_price = request.POST['p_price']
            pr_stock = request.POST['p_astock']
            pr_photo = request.FILES['p_photo']  

            product_exist = Product.objects.filter(p_number=pr_number).exists()  
            if not product_exist:
                add_products = Product(
                    p_name = pr_name,
                    p_number = pr_number,
                    p_details = pr_description,
                    p_price = pr_price,
                    p_stock = pr_stock,
                    p_image = pr_photo,
                    seller_id_id = request.session['s_id'] )                
                add_products.save()
                msg="Product Added Succesfully"
            else:
                 msg="product Already Added"

    return render(request,'reseller_app/add_product.html',{'status':msg})

def my_order(request):
    return render(request,'reseller_app/my_orders.html')


def update_stock(request):
    msg=''
    if request.method == 'POST':
        id = request.POST['pno'] 
        print(id)
        c_stock =int(request.POST['c_stock'])
        print(c_stock)
        n_stock =int( request.POST['n_stock'])
        u_stock =Product.objects.get(id=id)
        u_stock.p_stock = c_stock + n_stock
        u_stock.save()
        msg="stock updated successfully"
    return render(request,'reseller_app/update_stock.html',{'msg':msg})


def recent_orders(request):
    return render(request,'reseller_app/recent_orders.html')

def cancelled_orders(request):
    return render(request,'reseller_app/cancelled_orders.html')

def order_history(request):
    return render(request,'reseller_app/order_history.html')

def change_password(request):
    return render(request,'reseller_app/change_password.html')

def seller_ac(request):
    seller_P=Reseller.objects.get(id=request.session['s_id']) #select * from table where   
    return render(request,'reseller_app/seller_account.html',{'seller_details':seller_P})

def edit_ac(request):
    return render(request,'reseller_app/s_edit.html')

def seller_logout(request):
    del request.session['s_id']
    request.session.flush()
    return redirect('customer:home')

def get_product(request): 
             
    cat=request.POST['category']

    pno=Product.objects.filter(p_category=cat)   
    
    data=[{'id':pno1.id,'p_number':pno1.p_number} for pno1 in pno ]
    
    return JsonResponse({'data':data})

def get_stock(request): 
         
    pid=request.POST['p_no']   
    stock=Product.objects.get(id=pid)
  
    data=[{'p_stock':stock.p_stock}]
    return JsonResponse({'data':data})
    


   
    





 
 


