from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    message= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name
