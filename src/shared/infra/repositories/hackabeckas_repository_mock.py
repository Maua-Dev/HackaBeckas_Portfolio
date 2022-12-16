from typing import List
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
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
                      orderId=1, pizza=self.pizzas[0], table=self.tables[0]
      ),
                     Order(
                      orderId=2, pizza=self.pizzas[1], table=self.tables[1]
                     ),
                     Order(
                      orderId=3, pizza=self.pizzas[2], table=self.tables[2]
                     )
                     ]
        
    def create_order(self, new_order : Order) -> Order:
      for order in self.orders:
        if order.orderId == new_order.orderId:
          raise DuplicatedItem('orderId')     
      self.orders.append(order)
      return order
    
    def get_order(self, orderId: int) -> Order:
      for order in self.orders:
        if order.orderId == orderId:
          return order
      raise NoItemsFound('orderId')
    
    def get_all_orders(self) -> List[Order]:
      return self.orders