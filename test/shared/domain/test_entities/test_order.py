import pytest
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.order import Order
from src.shared.helpers.errors.domain_errors import TypeError
from src.shared.helpers.errors.domain_errors import EntityError

class Test_order():
    def test_order(self):
        order = Order(orderId=1, pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY), table=Table(tableNumber=1, numberOfPeople=2))
        
        assert order.orderId == 1
        assert order.pizza.flavor == FLAVOR.CALABRESA
        assert order.pizza.border == BORDER.CATUPIRY
        assert order.table.tableNumber == 1
        assert order.table.numberOfPeople == 2
    
    def test_order_orderId_must_be_int(self):
        with pytest.raises(TypeError):
            Order(orderId='Um', pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY), table=Table(tableNumber=1, numberOfPeople=2))
    
    def test_order_orderId_must_be_natural(self):
        with pytest.raises(EntityError):
            Order(orderId=-1, pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY), table=Table(tableNumber=1, numberOfPeople=2))