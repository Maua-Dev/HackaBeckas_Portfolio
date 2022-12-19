import pytest
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.modules.delete_order.app.delete_order_usecase import DeleteOrderUseCase
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

class Test_DeleteOrderUseCase:
    def test_delete_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = DeleteOrderUseCase(repo=repo)
        len_pretest = len(repo.orders)
        order = usecase(order=Order(
            orderId=1, 
            table=Table(tableNumber=1, numberOfPeople=2),
            pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY)
        ))
        assert len(repo.orders) == len_pretest-1
        assert order.table.tableNumber == 1
        assert order.table.numberOfPeople == 2
        assert order.pizza.flavor == FLAVOR.CALABRESA
        assert order.pizza.border == BORDER.CATUPIRY