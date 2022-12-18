import pytest
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.get_order.app.get_order_usecase import GetOrderUsecase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound

class Test_GetOrderUsecase:
    def test_get_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        
        order = usecase(orderId=repo.orders[1].orderId)
        
        assert repo.orders[1] == order
        
    def test_get_order_order_not_found(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            order = usecase(orderId=2004)
    
    def test_get_order_id_greater_than_zero(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            order = usecase(orderId=-4)