from django.db import models

# Create your models here.
class product(models.Model):
    SIZE_CHOICES=[
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra large')
    
    ]
    COLOUR_CHOICES= [
        ('Red','Red'),
        ('white','white'),
        ('pink','pink'),
        ('green','green'),
        ('black','black')
    ]
    
    name=models.CharField(max_length=200,null=True)
    size=models.CharField(max_length=2,choices=SIZE_CHOICES,default='M',null=True)
    colour=models.CharField(max_length=10,choices=COLOUR_CHOICES,default='Red',null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    image=models.ImageField(upload_to='product_img/',null=True)