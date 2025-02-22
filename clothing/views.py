from django.shortcuts import render
from clothing.models import product
from .forms import productForm
# Create your views here.
def clothing(request):
    form=productForm()
    pro_img=product.objects.all()
    if request.method=="POST":
        form=productForm(request.POST,request.FILES)
        if form.is_valid ():
            form.save()
            form=productForm()
    else:
        pro_img=product.objects.all()
    form =productForm()
    return render (request,'clothing/fashion.html',{'pro_img':pro_img,'form':form})