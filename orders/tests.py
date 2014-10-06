from django.test import TestCase

from orders.models import Order, OrderItem

import results


class OrderOrderingTestCase(TestCase):
    fixtures = ['test_orders.json']

    def test_orders_are_split_by_shipping_method(self):
        #fcm, pri = Order.split_by_shipping_method()
        self.assertEqual(results.fcm, fcm)
        self.assertEqual(results.pri, pri)

    def test_orders_are_split_by_single_and_multiple(self):
        #singles, multiples = Order.split_by_single_and_multiple()
        self.assertEqual(results.singles, singles)
        self.assertEqual(results.multiples, multiples)

    def test_single_orders_are_sorted(self):
        #single_sorted_orders = Order.single_orders_are_sorted()
        self.assertEqual(results.single_sorted_orders, single_sorted_orders)

    def test_multiple_orders_are_split_by_xxl_and_not(self):
        #xxl, not_xxl = Order.orders_split_by_xxl_and_not()
        self.assertEqual(results.xxl, xxl)
        self.assertEqual(results.not_xxl, not_xxl)