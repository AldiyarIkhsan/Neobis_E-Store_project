from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    status_choice = (
        ('ready', 'ready'),
        ('in process', 'in process'),
        ('closed', 'closed')
    )

    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choice, default='in process')
    products = models.ManyToManyField(Product)
    summ = models.FloatField(default=0, null=True, blank=True)


