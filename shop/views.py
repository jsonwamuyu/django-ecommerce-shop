from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('shop:product_list')  # Redirect to product list or homepage
    else:
        form = CustomUserCreationForm() # Initialize the form for GET request(unbound form) 
    return render(request, 'shop/register.html', {'form': form})


@login_required
def product_list(request):
    # This view should return a list of products
    # Assuming you have a Product model defined in models.py
    from .models import Product
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})    


@login_required
def cart(request):
    # This view should return the user's cart
    # Assuming you have a Cart model defined in models.py
    from .models import Cart
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})



@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list', product_id=product.id)  # Redirect to the product list or detail page
        # If the form is not valid, it will re-render the form with errors
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})


@login_required
def product_details(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    return render(request, 'shop/product_details.html', {'product': product})