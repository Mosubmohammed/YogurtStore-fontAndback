from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_modified=models.DateTimeField(User,auto_now=True)
    Phone=models.CharField(max_length=20,blank=True)
    Address1=models.CharField(max_length=200,blank=True)
    Address2=models.CharField(max_length=200,blank=True)
    City=models.CharField(max_length=200,blank=True)
    State=models.CharField(max_length=200,blank=True)
    Zipcode=models.CharField(max_length=200,blank=True)
    Country=models.CharField(max_length=200,blank=True)
    old_cart=models.CharField(max_length=1000,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.user.username
    
def Create_Profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

post_save.connect(Create_Profile,sender=User)
    
    
    
    
    
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural='Categories'
        
class Customer(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=10)
    Email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.First_name + self.Last_name}'
    

class Product(models.Model):
    Name=models.CharField(max_length=100)
    Price=models.DecimalField(default=0, max_digits=6,decimal_places=2)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Description=models.CharField(max_length=100,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/',blank=True,null=True)
    
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0, max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.Name
    

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Quantity=models.IntegerField(default=1)
    Address=models.CharField(max_length=50,default='',blank=True)
    phone=models.CharField(max_length=50,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product
    