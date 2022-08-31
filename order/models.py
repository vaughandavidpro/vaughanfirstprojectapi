from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):

    SIZES = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
    )

    STATUS = (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Not_Delivered','Not_Delivered'),

    )

    user_customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    size = models.CharField(max_length=50,choices=SIZES,default=SIZES[0][0])
    order_status = models.CharField(max_length=50,choices=STATUS,default=STATUS[2][0])
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f' Order by {self.user_customer.first_name} {self.user_customer.last_name} for {self.product} product'


