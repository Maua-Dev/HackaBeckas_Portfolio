from abc import ABC, abstractmethod
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR

class IHackabeckasRepository(ABC):
    
    @abstractmethod
    def create_order(self, tableNumber:int, numberOfPeople:int, flavor: FLAVOR, border: BORDER) -> Order:
        pass
    
    def delete_order():
        pass
    
    def get_order():
        pass
    
    def update_order():
        pass
    