import abc
from src.shared.helpers.errors.domain_errors import EntityError

class Table(abc.ABC):
    tableNumber: int
    numberOfPeople: int
    
    def __init__(self, tableNumber: int, numberOfPeople: int):
        if type(tableNumber) != int:
            raise EntityError("tableNumber must be int")
        if type(numberOfPeople) != int:
            raise EntityError("numberOfPeople must be int")
        self.tableNumber = tableNumber
        self.numberOfPeople = numberOfPeople