import unittest
from refactored_code import Order, OrderProcessor

class TestOrders(unittest.TestCase):

    def test_total_basic(self):
        o = Order("item", 10, 2)
        self.assertEqual(o.calculate_total(), 20)

    def test_zero_quantity(self):
        o = Order("item", 10, 0)
        self.assertEqual(o.calculate_total(), 0)

    def test_discount_applied(self):
        o = Order("item", 50, 3)  # 150
        self.assertEqual(o.calculate_total(), 135)

    def test_no_discount(self):
        o = Order("item", 10, 5)
        self.assertEqual(o.calculate_total(), 50)

    def test_processor(self):
        orders = [Order("a", 10, 2), Order("b", 50, 3)]
        processor = OrderProcessor()
        result = processor.process_orders(orders)
        self.assertEqual(result, [20, 135])

    # 🔽 ДОДАНІ ТЕСТИ

    def test_negative_quantity(self):
        o = Order("item", 10, -5)
        self.assertEqual(o.calculate_total(), 0)

    def test_large_values(self):
        o = Order("item", 1000, 10)
        self.assertEqual(o.calculate_total(), 9000)

    def test_zero_price(self):
        o = Order("item", 0, 10)
        self.assertEqual(o.calculate_total(), 0)

    def test_discount_edge(self):
        o = Order("item", 50, 2)  # 100
        self.assertEqual(o.calculate_total(), 100)

    def test_discount_above_edge(self):
        o = Order("item", 50, 3)  # 150
        self.assertEqual(o.calculate_total(), 135)

    def test_processor_empty(self):
        processor = OrderProcessor()
        self.assertEqual(processor.process_orders([]), [])

    def test_processor_with_none(self):
        processor = OrderProcessor()
        orders = [None, Order("a", 10, 1)]
        self.assertEqual(processor.process_orders(orders), [10])

    def test_float_price(self):
        o = Order("item", 10.5, 2)
        self.assertEqual(o.calculate_total(), 21.0)

    def test_single_item(self):
        o = Order("item", 99, 1)
        self.assertEqual(o.calculate_total(), 99)

    def test_high_quantity(self):
        o = Order("item", 1, 200)
        self.assertEqual(o.calculate_total(), 180)