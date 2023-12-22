from datetime import timezone

from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    stock=models.IntegerField(default=0)   # New field for stock
    def __str__(self):
        return self.name
    def is_in_stock(self):
        return self.stock>0
    def reduce_stock(self ,quantity):
        if quantity > self.stock:
            return False
        self.stock-=quantity
        self.save()
        return True
    def increase_stovk(self,amount):
        self.stock +=amount
        self.save()
    class Meta:
        ordering=['name']


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating}"


class FlashSale(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    discount_percentage=models.PositiveIntegerField()  # e.g., 20 means 20% off
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def is_active(self):
        now=timezone.now()
        return self.start_time <= now <= self.end_time

    class Meta:
        unique_together= ('product','start_time','end_time')


class ProductViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)










