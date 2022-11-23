from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR

class HackabeckasRepositoryMock(IHackabeckasRepository):
    orders = list[Order]
    
    def __init__(self):
        self.orders = [
            Order(
                pizza= Pizza(flavor=FLAVOR.CALABRESA, border=None),
                table= Table(tableNumber=1, numberOfPeople=2)
                  ),
            
            Order(
                pizza= Pizza(flavor=FLAVOR.ATUM, border=BORDER.CATUPIRY),
                table= Table(tableNumber=218, numberOfPeople=8)
                  ),
            
            Order(
                pizza= Pizza(flavor=FLAVOR.QUATRO_QUEIJOS, border=BORDER.CHEDDAR),
                table= Table(tableNumber=0, numberOfPeople=1)
                  ),
            
        ]
        
    def create_order(self, tableNumber:int, numberOfPeople:int, flavor: FLAVOR, border: BORDER) -> Order:
        order = Order(
            pizza=Pizza(flavor=flavor, border=border),
            table=Table(tableNumber=tableNumber, numberOfPeople=numberOfPeople)
        )
        self.orders.append(order)
        
        return order