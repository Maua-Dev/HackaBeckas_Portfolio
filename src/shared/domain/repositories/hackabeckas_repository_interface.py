from abc import ABC, abstractmethod
from src.shared.domain.entities.order import Order
from typing import List

class IHackabeckasRepository(ABC):
    
    @abstractmethod
    def create_order(self, order : Order) -> Order:
        '''
        if order duplicated, raise DuplicatedItem error
        '''
        pass
    
    @abstractmethod
    def get_order(self, orderId: int) -> Order:
        # If order not found, raise ItemsNotFound error
        pass
    
    @abstractmethod
    def get_all_orders(self) -> List[Order]:
        pass
    
    @abstractmethod
    def delete_order(self) -> Order:
        pass
    