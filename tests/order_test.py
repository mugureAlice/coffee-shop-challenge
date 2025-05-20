import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order():
    Joe = Customer("Joe")
    Makiatto  = Coffee(" Makiatto ")
    order = Order(Joe,  Makiatto , 5.0)

assert order.customer == Joe
assert order.coffee ==  Makiatto 
assert order.price == 5.0

with pytest.raises(ValueError):
    Order(Joe, latte, 0)