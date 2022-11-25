from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR

class HackabeckasRepositoryMock(IHackabeckasRepository):
    pizzas = list[Pizza]
    tables = list[Table]
    orders = list[Order]
    
    def __init__(self):
      
      self.pizzas = [Pizza(
                        flavor=FLAVOR.ATUM, border=None
      ),
                     Pizza(
                       flavor=FLAVOR.MUSSARELA, border=BORDER.CATUPIRY
                     ),
                     Pizza(
                       flavor=FLAVOR.CALABRESA, border=BORDER.CHEDDAR
                     )]
      self.tables = [Table(
                        tableNumber=1,
                        numberOfPeople=2
      ),
                     Table(
                       tableNumber=14,
                       numberOfPeople=4
                     ),
                     Table(
                       tableNumber=12,
                       numberOfPeople=6
                     )]
      self.orders = [Order(
                      id=1, pizza=self.pizzas[0], table=self.tables[0]
      ),
                     Order(
                      id=2, pizza=self.pizzas[1], table=self.tables[1]
                     ),
                     Order(
                      id=3, pizza=self.pizzas[2], table=self.tables[2]
                     )
                     ]
        
    def create_order(self, id: int, tableNumber: int, numberOfPeople: int, flavor: FLAVOR, border: BORDER) -> Order:
      order = Order(
        id=id,
        pizza=Pizza(flavor=flavor, border=border),
        table=Table(tableNumber=tableNumber, numberOfPeople=numberOfPeople)
      )
      self.orders.append(order)
      return order