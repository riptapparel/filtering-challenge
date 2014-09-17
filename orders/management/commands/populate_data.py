import datetime
import random
from django.core.management.base import BaseCommand
from orders.models import Order, OrderItem


class Command(BaseCommand):
    help = 'populates a sample set of data for the interview test'

    def handle(self, *args, **options):
        return  # PREVENT TO RUN THIS COMMAND

        Order.objects.filter().delete()
        OrderItem.objects.filter().delete()

        for i in range(0, 100):
            random_shipping_choice_index = random.randrange(0, 2)
            order = Order.objects.create(
                shipping_method=Order.SHIPPING_CHOICES[random_shipping_choice_index][0],
                date_completed=datetime.datetime.now()
            )
            random_number_of_items = random.randrange(1, 5)
            for n in range(0, random_number_of_items):
                random_choice_index = random.randrange(0, 6)
                OrderItem.objects.create(
                    order=order,
                    product=OrderItem.PRODUCT_CHOICES[random_choice_index][0],
                    quantity=random.randrange(1, 3)
                )
