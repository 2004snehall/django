from django.shortcuts import render,get_object_or_404,redirect
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

#view to edit a product
def edit_product(request,product_id):
    Product=get_object_or_404(product,id=product_id)
    
    if request.method=="POST":
        form=productForm(request.POST,request.FILES,instance=Product)
        if form.is_valid():
            form.save()
            return redirect('clothing')
    else:
        form=productForm(instance=Product)
        
    return render(request,'clothing/edit_product.html',{'form':form})
                                        
#view to delete a product
def delete_product(request,product_id):
    Product=get_object_or_404(product,id=product_id)
    
    if request.method=="POST":
        Product.delete()
        return redirect('clothing')
    
    return render(request,'clothing/confirm_delete.html',{Product:'product'})