import pytest
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.delete_order.app.delete_order_viewmodel import DeleteOrderViewModel
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.entities.order import Order

class Test_DeleteOrderViewModel:
     def test_delete_order_viewmodel(self):
        repo = HackabeckasRepositoryMock()
        
        orderViewModel = DeleteOrderViewModel(order=Order(
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
            "message" : "The order has been deleted"
        }
        assert orderViewModel == expected