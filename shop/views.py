from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('shop:product_list')  # Redirect to product list or homepage
    else:
        form = CustomUserCreationForm(request.POST)
    return render(request, 'shop/register.html', {'form': form})


def product_list(request):
    # This view should return a list of products
    # Assuming you have a Product model defined in models.py
    from .models import Product
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})    