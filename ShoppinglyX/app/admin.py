from django.contrib import admin
from django.contrib.auth.models import User

from .models import (Product,Customer,OrderPlaced,Cart)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','selling_price','discounted_price','description','brand','category','product_image']
    
    


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','locality','city','zipcode','state']
    
    
@admin.register(Cart)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity']
    
    
@admin.register(OrderPlaced)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','ordered_date','status']