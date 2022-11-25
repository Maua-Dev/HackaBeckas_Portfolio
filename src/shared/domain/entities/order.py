import abc

from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR

class Order(abc.ABC):
    id: int
    pizza: Pizza
    table: Table
    
    def __init__(self, id: int, pizza: Pizza, table: Table):
        if (type(id) != int):
            raise TypeError('id', 'int')
        if (id < 0):
            raise ValueError('id must be greater than 0')
        if (pizza == None or type(pizza) != Pizza):
            raise TypeError('pizza', 'Pizza')
        if (pizza.border == None or type(pizza.border) != BORDER):
            raise TypeError('pizza.border', 'BORDER')
        if (pizza.flavor == None or type(pizza.flavor) != FLAVOR):
            raise TypeError('pizza.flavor', 'FLAVOR')
        self.pizza = pizza
        
        if (table == None or type(table) != Table):
            raise TypeError('table', 'Table')
        if (table.numberOfPeople == None or type(table.numberOfPeople) != int):
            raise TypeError('table.numberOfPeople', 'int')
        if (table.tableNumber == None or type(table.tableNumber) != int):
            raise TypeError('table.tableNumber', 'int')
        self.table = table