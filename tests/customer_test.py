import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    # Fixed variable name mismatch (Joe vs james)
    joe = Customer("Joe")
    assert joe.name == "Joe"

def test_customer_validation():
    # Moved the ValueError test into a proper test function
    with pytest.raises(ValueError):
        Customer("")