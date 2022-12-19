from abc import ABC, abstractmethod
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR

class IHackabeckasRepository(ABC):
    
    @abstractmethod
    def create_order(self, order : Order) -> Order:
        pass

    @abstractmethod
    def update_order(self, orderId, newFlavor : FLAVOR, newBorder : BORDER, new_table: int, new_number_of_people: int) -> Order:
        pass