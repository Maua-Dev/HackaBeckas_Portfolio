from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository


class GetOrderUsecase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo
    
    def __call__(self, orderId: int) -> Order:
        return self.repo.get_order(orderId)