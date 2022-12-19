from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table

class TableViewModel:
    table: Table
    
    def __init__(self, table: Table):
        self.table = table
    def to_dict(self) -> dict:
        return  {
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

class OrderViewModel:
    order: Order

    def __init__(self, order: Order):
        self.order = order
    def to_dict(self) -> dict:
        return {
           "orderId" : self.order.orderId,
            "table" : self.order.table,
            "pizza" : self.order.pizza
        }

class DeleteOrderViewModel:
    order: Order

    def __init__(self, order:Order):
        self.order = order
    def to_dict(self) -> dict:
        return {
            "orderId" : OrderViewModel(self.order.orderId).to_dict(),
            "table" : TableViewModel(self.order.table).to_dict(),
            "pizza" : PizzaViewModel(self.order.pizza).to_dict(),
            "message": "the order has been deleted",
        }