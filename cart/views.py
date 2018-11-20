from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from products.models import Product
import json
# Create your views here.



def adding_to_cart(request):
    
    cart = request.session.get('cart',{})
    quantity = int(request.POST['quantity'])
    product = request.POST['product']
    
    cart[product]= cart.get(product, 0) + quantity
    
    request.session['cart'] = cart
    

    return redirect('/')

def view_cart(request):
    cart = request.session.get('cart', {})
    
    
    cart_items = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
    
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': product.price * quantity
        })    
    
    return render(request, "cart/view_cart.html", {'cart_items': cart_items})
