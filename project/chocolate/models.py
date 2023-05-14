from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=250)

    def __str__(self):
        return self.title



class Chocolate(models.Model):
    title=models.CharField(max_length=200)
    catagory=models.ForeignKey(Category,related_name='chocolates',on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    price=models.FloatField(null=True,blank=True)
    image_url=models.URLField(max_length=2080)
    choco_available=models.BooleanField()
    is_deleted=models.BooleanField()

    def __str__(self):
        return self.title

 #it is a decorator    
    @property
    def name(self):
        return self.title


class Carts(models.Model):
    product=models.ForeignKey(Chocolate,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    date= models.DateField(auto_now_add=True)
    options=(
        ('id-cart','in-cart'),
        ('order-placed','order-placed'),
        ('removed','removed')
    )
    status =models.CharField(max_length=100,choices=options,default='in-cart')

