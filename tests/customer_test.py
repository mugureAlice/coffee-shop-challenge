import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    
    
    joe = Customer("Joe")
    assert joe.name == "Joe"

def test_customer_validation():
   
    with pytest.raises(ValueError):
        Customer("")