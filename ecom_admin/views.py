from django.shortcuts import render,redirect
from reseller_app.models import Reseller
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def admin_home(request):
    return render(request,'ecom_admin/admin_home.html')

def approve_resellers(request):    
    reseller = Reseller.objects.filter(s_status = "pending")
    #reseller = Reseller.objects.all()
    return render(request,'ecom_admin/approve_resellers.html',{'pending':reseller})

def customers_list(request):
    return render(request,'ecom_admin/customers_list.html')

def registered_resellers(request):
    return render(request,'ecom_admin/registered_resellers.html')

def change_password(request):
    return render(request,'ecom_admin/change_password.html')

def admin_login(request):
    return render(request,'ecom_admin/adminlogin.html')

def r_approve(request,reseller_id):
    reseller= Reseller.objects.filter(id=reseller_id).update(s_status="approved")
    reseller1=Reseller.objects.get(id=reseller_id)
    subject = 'welcome to ecommerce  world'
    message = f'Hi {reseller1.s_name}, thank you for registering in ecommerce application.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['anupamaunni612@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return redirect('ecom_admin:approve_reseller')



