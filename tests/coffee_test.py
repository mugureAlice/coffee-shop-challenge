import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file), '..')))

import pytest
from coffee import Coffee

def test_coffee_name():
    Makiatto = Coffee(" Makiatto ")
    assert latte.name == " Makiatto "

with pytest.raises(ValueError):
    Coffee("T")  
