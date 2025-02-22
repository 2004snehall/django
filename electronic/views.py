from django.shortcuts import render,HttpResponse
from .models import Product
# Create your views here.
def home(request):
    prod=Product.objects.all()
    return render(request,"electronic/home.html",{"prod":prod})



























