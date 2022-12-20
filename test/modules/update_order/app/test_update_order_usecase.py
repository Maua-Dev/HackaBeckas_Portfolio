import pytest
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.update_order.app.update_order_usecase import UpdateOrderUseCase
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound, DuplicatedItem
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER

class Test_UpdateOrderUseCase:
    def test_update_order_usecase_flavor(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo)
        usecase(1, FLAVOR.MARGUERITA)
        order = repo.orders[0]
        assert order.pizza.flavor == FLAVOR.MARGUERITA

    def test_update_order_usecase_border(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo)
        usecase(1, new_border=BORDER.CHEDDAR)
        order = repo.orders[0]
        assert order.pizza.border == BORDER.CHEDDAR

    def test_update_order_usecase_table(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo)
        usecase(1, new_table=2)
        order = repo.orders[0]
        assert order.table.tableNumber == 2

    def test_update_order_usecase_number_of_people(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo)
        usecase(1, new_number_of_people=5)
        order = repo.orders[0]
        assert order.table.numberOfPeople == 5

    def test_update_order_usecase_non_existent_orderId(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo)
        with pytest.raises(NoItemsFound):
            usecase(orderId=4)

    def test_update_order_usecase_invalid_orderId(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo)
        with pytest.raises(EntityError):
            usecase(orderId='invalid')