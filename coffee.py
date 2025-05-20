class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def get_name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all_orders if order.get_coffee() == self]

    def customers(self):
    unique_customers = set()
    for order in self.orders():
        unique_customers.add(order.get_customer())
    return list(unique_customers)
