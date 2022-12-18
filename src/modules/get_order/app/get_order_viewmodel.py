from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.entities.order import Order

class TableViewModel:
    table: Table
    
    def __init__(self, table: Table):
        self.table = table
        
    def to_dict(self) -> dict:
        return {
            "tableNumber" : self.table.tableNumber,
            "numberOfPeople" : self.table.numberOfPeople
        }

class PizzaViewModel:
    pizza: Pizza
    
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
    
    def to_dict(self) -> dict:
        return {
            "flavor" : self.pizza.flavor.value,
            "border" : self.pizza.border.value
        }
    

class GetOrderViewmodel:
    orderId: int
    table: TableViewModel
    pizza: PizzaViewModel
    
    def __init__(self, order: Order):
        self.orderId = order.orderId
        self.table = TableViewModel(table=order.table)
        self.pizza = PizzaViewModel(pizza=order.pizza)
        
    def to_dict(self):
        return {
            'orderId' : self.orderId,
            'table' : self.table.to_dict(),
            'pizza' : self.pizza.to_dict()
        }