class Customer:
    def __init__(self, name):
        self.set_name(name) 

    def get_name(self):
        return self._name  

    def set_name(self, value):
        
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.get_customer() == self]

     def coffees(self):
        unique_coffees = set()
        for order in self.orders():
            unique_coffees.add(order.get_coffee())
        return list(unique_coffees)    
        
    def create_order(self, coffee, price):
    return Order(self, coffee, price)
    
