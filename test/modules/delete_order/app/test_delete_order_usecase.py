import pytest
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.modules.delete_order.app.delete_order_usecase import DeleteOrderUsecase

from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

class Test_DeleteOrderUsecase:
    def test_delete_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = DeleteOrderUsecase(repo=repo)
        
        len_before = len(repo.orders)
        order = usecase(orderId=repo.orders[1].orderId)
        expected = Order(
            orderId=2,
            table = Table(
                    tableNumber=14,
                    numberOfPeople=4
                     ),
            pizza =  Pizza(
                       flavor=FLAVOR.MUSSARELA, border=BORDER.CATUPIRY
                     )
        )
        assert len_before == len(repo.orders) + 1
        assert [order.orderId, order.pizza.flavor.value, order.pizza.border.value, order.table.tableNumber, order.table.numberOfPeople] == [expected.orderId, expected.pizza.flavor.value, expected.pizza.border.value, expected.table.tableNumber, expected.table.numberOfPeople]
        
    def test_delete_order_not_found(self):
        repo = HackabeckasRepositoryMock()
        usecase = DeleteOrderUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            usecase(orderId=123)