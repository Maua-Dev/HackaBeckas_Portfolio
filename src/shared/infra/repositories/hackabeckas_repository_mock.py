from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.domain_errors import EntityError

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
        
    def create_order(self, order : Order) -> Order:
      self.orders.append(order)
      return order

    def update_order(self, orderId, newFlavor: FLAVOR = None, newBorder: BORDER = None, new_table: int= None, new_number_of_peopler: int = None) -> Order:
      if not Order.validade_id(orderId):
           raise EntityError('orderId')

      updated_order = None
      for order in self.orders:
        if order.orderId == orderId:
          updated_order = order
          break
      
      if updated_order == None:
        raise NoItemsFound('orderId')

      if type(newFlavor) == FLAVOR and newFlavor != None:
          updated_order.pizza.flavor = newFlavor

      if type(newBorder) == BORDER and newBorder != None:
          updated_order.pizza.border = newBorder

      if type(new_table) == int and new_table != None:
          updated_order.table.tableNumber = new_table

      if type(new_number_of_peopler) == int and new_number_of_peopler != None:
          updated_order.table.numberOfPeople = new_number_of_peopler

      
