import pytest
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.create_order.app.create_order_usecase import CreateOrderUseCase

class Test_CreateOrderUseCase:
    def test_create_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        len_pretest = len(repo.orders)
        order = usecase(order=Order(
            orderId=45, 
            table=Table(tableNumber=1, numberOfPeople=2),
            pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY)
        ))
        assert len(repo.orders) == len_pretest+1
        assert order.orderId == 45
        assert order.table.tableNumber == 1
        assert order.table.numberOfPeople == 2
        assert order.pizza.flavor == FLAVOR.CALABRESA
        assert order.pizza.border == BORDER.CATUPIRY
    
    def test_create_order_usecase_duplicated_item(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        len_pretest = len(repo.orders)
        with pytest.raises(DuplicatedItem):
            order = usecase(order=Order(
            orderId=1, 
            table=Table(tableNumber=1, numberOfPeople=2),
            pizza=Pizza(flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY)
            ))
            
