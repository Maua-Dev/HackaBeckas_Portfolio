import pytest
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.create_order.app.create_order_usecase import CreateOrderUseCase

class Test_CreateOrderUsecase:
    def test_create_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        len_pretest = len(repo.orders)
        order = usecase(orderId=1, tableNumber=1, numberOfPeople=2, flavor=FLAVOR.CALABRESA, border=BORDER.CATUPIRY)
        assert len(repo.orders) == len_pretest+1
        assert order.table.tableNumber == 1
        assert order.table.numberOfPeople == 2
        assert order.pizza.flavor == FLAVOR.CALABRESA
        assert order.pizza.border == BORDER.CATUPIRY
