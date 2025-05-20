import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file), '..')))

import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    Joe = Customer("Joe")
    assert james.name == "Joe"

with pytest.raises(ValueError):
    Customer("")  