from src.modules.get_order.app.get_order_viewmodel import GetOrderViewmodel
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.order import Order


class Test_GetOrderViewmodel:
    def test_get_order_viewmodel(self):
        order = Order(
            orderId=1,
            table=Table(
                numberOfPeople=1,
                tableNumber=1
            ),
            pizza=Pizza(
                flavor=FLAVOR.CALABRESA,
                border=BORDER.CATUPIRY
            )
        )
        orderViewModel = GetOrderViewmodel(order=order).to_dict()
        
        expected = {
            'orderId' : 1,
            'table' : {
                'numberOfPeople' : 1,
                'tableNumber' : 1
            },
            'pizza' : {
                'flavor' : 'CALABRESA',
                'border' : 'CATUPIRY'
            }
        }
        
        assert expected == orderViewModel