from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository


class GetOrderUsecase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo
    
    def __call__(self, orderId: int) -> Order:
        if orderId < 1:
            raise EntityError('orderId')
        order = self.repo.get_order(orderId=orderId)
        if order == None:
            raise NoItemsFound('orderId')
        return order
