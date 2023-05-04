from django.db import models

from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name: "category"
        verbose_name_plural: "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name: "product"
        verbose_name_plural: "products"

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
