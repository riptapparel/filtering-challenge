from django.test import TestCase

from orders.models import Order, OrderItem


class OrderOrderingTestCase(TestCase):
    fixtures = ['test_orders.json']

    def test_orders_are_split_by_shipping_method(self):
        #todo: write tests for fun and profit.
        pass

    def test_orders_are_split_by_single_and_multiple(self):
        #todo: write tests for fun and profit.
        pass

    def test_single_orders_are_sorted(self):
        #todo: write tests for fun and profit.
        pass

    def test_multiple_orders_are_split_by_xxl_and_not(self):
        #todo: write tests for fun and profit.
        pass
