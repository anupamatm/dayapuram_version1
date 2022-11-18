from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('',views.customer_home,name='home'),
    path('my-cart',views.my_cart, name='cart'),
    path('my-order',views.my_order, name='order'),
    path('p-detail/<int:product_id>',views.product_detail, name='product_detail'),
    path('myaccount',views.my_ac, name='my-account'),
    path('edit',views.edit_form, name='my-edit'),
    path('select_address',views.select_address, name='select_address'),
    path('c_payment',views.c_payment, name='c_payment'),
    path('c_logout',views.c_logout, name='c_logout'),
    path('view_cart',views.view_cart, name='view_cart'),
    path('del_cart_item/<int:product_id>',views.del_cart_item, name='del_cart_item'),
    path('e_exists',views.email_exist,name="e_exists"),
    path('change_qty',views.change_qty,name="change_qty"),
  
]