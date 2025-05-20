class order:
    def _init_(self,customer, coffee, price): if not isinstance(price, float) or not (1.0 <= price <= 10.0):
           return("Price must be a float between 1.0 and 10.0.")
        self.customer = customer
        self.coffee = coffee
        self.price = price

     def get_price(self):
        return self._price
    