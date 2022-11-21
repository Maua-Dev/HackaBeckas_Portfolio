import pytest

from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.helpers.errors.domain_errors import TypeError

class Test_pizza():
    def test_pizza(self):
        pizza = Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY)
        
        assert pizza.flavor == FLAVOR.CALABRESA
        assert pizza.border == BORDER.CATUPIRY
    
    def test_pizza_flavor_must_be_FLAVOR(self):
        with pytest.raises(TypeError):
            pizza = Pizza(flavor=1)
    
    def test_pizza_borda_must_be_BORDER(self):
        with pytest.raises(TypeError):
            pizza = Pizza(flavor=FLAVOR.CALABRESA, border=1)