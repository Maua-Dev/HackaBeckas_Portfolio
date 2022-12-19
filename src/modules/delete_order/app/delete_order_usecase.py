from src.shared.domain.entities.order import Order

from src.shared.infra.repositories.hackabeckas_repository_mock import IHackabeckasRepository

class DeleteOrderUseCase:
    def __init__(self, repo:IHackabeckasRepository):
        self.repo = repo
        
    def __call__(self, order: Order) -> Order:
        return self.repo.delete_order(order=order)
