import abc
from src.shared.helpers.errors.domain_errors import TypeError

class Table(abc.ABC):
    tableNumber: int
    numberOfPeople: int
    
    def __init__(self, tableNumber: int, numberOfPeople: int):
        if type(tableNumber) != int:
            raise TypeError('tableNumber', 'int')
        if type(numberOfPeople) != int:
            raise TypeError('numberOfPeople', 'int')
        self.tableNumber = tableNumber
        self.numberOfPeople = numberOfPeople