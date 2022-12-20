from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository


class DeleteOrderUsecase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo
    
    def __call__(self, orderId: int) -> None:
        order = self.repo.delete_order(orderId=orderId)
        return order