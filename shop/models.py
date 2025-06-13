from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, help_text="Name of the product")
    description = models.TextField(help_text="Describe the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the product")
    stock_quantity = models.PositiveIntegerField(help_text="Products in stock")
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # fixed

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['product_name']

class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", 'Pending'),
        ("PAID", 'Paid'),
        ("SHIPPED", 'Shipped'),
        ('DELIVERED', "Delivered"),
        ("CANCELLED", "Cancelled")
    ]
    PAYMENT_STATUS = [
        ("PAID", 'Paid'),
        ("UNPAID", "Unpaid")
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, help_text="Customer who owns the order")
    order_date = models.DateTimeField(auto_now_add=True, help_text="Date and time order placed")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total price")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING", help_text="Status of the order")
    shipping_address = models.TextField(help_text="Shipping address for the order")  # changed to TextField
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="UNPAID", help_text="Payment status of the order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # fixed

    def __str__(self):
        return f"Order {self.id} placed by {self.user.username if self.user else 'Unknown'}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-order_date"]  # descending order for recent first

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # fixed

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} (Order {self.order.id})"
    
    def get_subtotal(self):
        return self.quantity * self.unit_price
    
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
        ordering = ["created_at"]

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # fixed

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # fixed

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"

    def get_total_price(self):
        return self.product.price * self.quantity

    class Meta:
        unique_together = ('cart', 'product')
