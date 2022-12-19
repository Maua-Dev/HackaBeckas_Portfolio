from src.shared.domain.entities.table import Table
from src.modules.update_order.app.update_order_viewmodel import UpdateOrderViewModel
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
import pytest

class Test_UpdateOrderViewModel:
    def test_update_student_view_model(self):
        repo = HackabeckasRepositoryMock()

        result = {
            "orderId" : 1,
            "table" : {
                "tableNumber" : 1,
                "numberOfPeople" : 2
            },
            "pizza" : {
                "flavor" : "FRANGO",
                "border" : "CATUPIRY"
            },
            "message" : "Order was updated successfully"
       }

        orderViewModel = UpdateOrderViewModel(order=Order(orderId= 1, pizza=Pizza(flavor=FLAVOR.FRANGO, border=BORDER.CATUPIRY), table=Table(tableNumber=1, numberOfPeople=2))).to_dict()

        assert orderViewModel == result