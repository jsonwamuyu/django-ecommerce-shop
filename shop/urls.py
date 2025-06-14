from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:product_list'), name='logout'),
    path('', views.product_list, name='product_list'),  # Default to product list
    path('cart/', views.cart, name='cart'),
]
