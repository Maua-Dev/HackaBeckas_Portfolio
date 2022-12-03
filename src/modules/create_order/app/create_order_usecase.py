from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository


class CreateOrderUseCase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo
        
    def __call__(self, order : Order) -> Order:
        return self.repo.create_order(order)

