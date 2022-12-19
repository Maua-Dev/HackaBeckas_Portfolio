import abc

from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.helpers.errors.domain_errors import TypeError
from src.shared.helpers.errors.domain_errors import EntityError

class Order(abc.ABC):
    orderId: int
    pizza: Pizza
    table: Table
    
    def __init__(self, orderId: int, pizza: Pizza, table: Table):
        
        if (type(orderId) != int):
            raise TypeError('orderId', 'int')
        
        if (orderId < 0):
            raise EntityError('orderId')
        
        self.orderId = orderId
        
        if (pizza == None or type(pizza) != Pizza):
            raise TypeError('pizza', 'Pizza')

        self.pizza = pizza
        
        if (table == None or type(table) != Table):
            raise TypeError('table', 'Table')
        
        self.table = table