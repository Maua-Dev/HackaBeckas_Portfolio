import pytest
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.modules.create_order.app.create_order_viewmodel import CreateOrderViewModel
from src.shared.domain.entities.order import Order
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

class Test_CreateOrderViewModel:
    def test_create_order_viewmodel(self):
        repo = HackabeckasRepositoryMock()
        
        orderViewModel = CreateOrderViewModel(order=Order(
            orderId=1,
            table=Table(tableNumber=1, numberOfPeople=2),
            pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY)
        )).to_dict()
        
        expected = {
            "orderId" : 1,
            "table" : {
                "tableNumber" : 1,
                "numberOfPeople" : 2
            },
            "pizza" : {
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            },
            "message" : "The order has been created"
        }
        
        assert orderViewModel == expected