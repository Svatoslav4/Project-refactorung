DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

class Order:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self) -> float:
        if self.quantity <= 0:
            return 0

        total = self.price * self.quantity
        return self.apply_discount(total)

    def apply_discount(self, total: float) -> float:
        if total > DISCOUNT_THRESHOLD:
            return total * DISCOUNT_RATE
        return total


class OrderProcessor:
    def process_orders(self, orders: list[Order]) -> list[float]:
        results = []

        for order in orders:
            if order is None:
                continue

            total = order.calculate_total()
            results.append(total)

        return results