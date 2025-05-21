from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),    
    path('index',index,name='index'),
    path('login',login,name='login'),
    path('resetpassword',resetpassword,name='resetpassword'),
    path('add_product',add_product,name='add_product'),
    path('display_product',display_product,name='display_product'),
    path('edit_product',edit_product,name='edit_product'),
    path('add_category',add_category,name='add_category'),
    path('add_brand',add_brand,name='add_brand'),
    path('display_category',display_category,name='display_category'),
    path('display_brand',display_brand,name='display_brand'),
    path('display_user',display_user,name='display_user'),
    path('display_admin',display_admin,name='display_admin'),
    path('display_orders',display_orders,name='display_orders'),
    path('display_orderdetails',display_orderdetails,name='display_orderdetails'),
    path('edit_orderdetails',edit_orderdetails,name='edit_orderdetails'),
    path('display_cart',display_cart,name='display_cart'),
    path('display_wishlist',display_wishlist,name='display_wishlist'),
    path('display_payment',display_payment,name='display_payment'),
    path('report_FBT_Report',report_FBT_Report,name='report_FBT_Report'),
    path('report_customer',report_customer,name='report_customer'),
    path('report_sales',report_sales,name='report_sales'),
]