from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to="category-images/%Y/%m/%d/", blank=True, default="image.png")

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to="product-images/%Y/%m/%d/", blank=True, default="image.png")
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

