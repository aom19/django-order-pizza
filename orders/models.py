

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User=get_user_model()

# Create your models here.
class Order(models.Model):
    PIZZA_SIZES=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large')

    )

    ORDER_STATUSES=(
        ('P','Pending'),
        ('C','Completed'),
        ('D','Delivered'),
        ('R','Rejected')

    )

    order_status=models.CharField(max_length=25,choices=ORDER_STATUSES,default=ORDER_STATUSES[0][0])
    size=models.CharField(max_length=25,choices=PIZZA_SIZES,default=PIZZA_SIZES[0][0])
    quantity=models.IntegerField()
    flavour=models.CharField(max_length=40)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    placed_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.flavour} by {self.customer}>"