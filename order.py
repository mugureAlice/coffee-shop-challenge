class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer object.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee object.")
        if not (isinstance(price, float) and 1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    def get_customer(self):
        if not isinstance(self._customer, Customer):
            raise TypeError("Stored customer is not a Customer object.")
        return self._customer


    def get_coffee(self):
        if not isinstance(self._coffee, Coffee):
            raise TypeError("Stored coffee is not a Coffee object.")
        return self._coffee

    def get_price(self):
        return self._price 
        
   def orders(self):
    return [order for order in Order.all_orders if order.get_customer() == self]
   
     