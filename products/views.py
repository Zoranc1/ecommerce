from django.shortcuts import render, get_object_or_404,redirect
from .models import Product

# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request,'products/product_list.html', {'products':products})
    
def products_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    
    return render(request, "products/product_detail.html",{'product':product})