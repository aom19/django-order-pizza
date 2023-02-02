from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','flavour','size','order_status','size' ,'created_at']
    list_filter=['order_status' , 'size','created_at']
