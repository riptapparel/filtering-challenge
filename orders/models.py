from django.db import models


class Order(models.Model):
    FCM = 'FCM'
    PRI = 'PRI'
    SHIPPING_CHOICES = (
        ('FCM', 'First Class Mail'),
        ('PRI', 'Priority Mail'),
    )
    shipping_method = models.CharField(max_length=100, choices=SHIPPING_CHOICES)
    date_completed = models.DateTimeField()


class OrderItem(models.Model):
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'
    PRODUCT_CHOICES = (
        ('XS', 'Extra Small Tee'),
        ('S', 'Small Tee'),
        ('M', 'Medium Tee'),
        ('L', 'Large Tee'),
        ('XL', 'Extra Large Tee'),
        ('XXL', 'Double Extra Large Tee'),
    )
    priority = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
    order = models.ForeignKey(Order, related_name='items')
    product = models.CharField(max_length=100, choices=PRODUCT_CHOICES)
    quantity = models.PositiveIntegerField(default=1)