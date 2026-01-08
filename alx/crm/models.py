from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    products = models.ManyToManyField(Product, related_name='orders')

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

    def calculate_total_amount(self):
        total = sum(product.price for product in self.products.all())
        self.total_amount = total
        self.save()
        return total
