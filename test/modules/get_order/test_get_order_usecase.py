import pytest
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.get_order.app.get_order_usecase import GetOrderUsecase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound

class Test_GetOrderUsecase:
    def test_get_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        
        user = usecase(orderId=repo.orders[1].orderId)
        
        assert repo.orders[1] == user
        
    def test_get_order_user_not_found(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            user = usecase(orderId=2004)