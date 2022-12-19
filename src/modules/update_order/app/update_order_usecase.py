from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError

class UpdateOrderUseCase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo

    def __call__(self, orderId, new_flavor:FLAVOR = None, new_border: BORDER = None, new_table: int = None, new_number_of_people: int = None) -> Order:
        if not Order.validade_id(orderId):
            raise EntityError('orderId')

        if type(new_flavor) != FLAVOR and new_flavor != None:
            raise EntityParameterTypeError('new_flavor must be FLAVOR')

        if type(new_border) != BORDER and new_border != None:
            raise EntityParameterTypeError('new_border must be BORDER')

        if type(new_table) != int and new_table != None:
            raise EntityParameterTypeError('new_table must be int')

        if type(new_number_of_people) != int and new_number_of_people != None:
            raise EntityParameterTypeError('new_number_of_people must be int')

        return self.repo.update_order(orderId, new_flavor, new_border, new_table, new_number_of_people)