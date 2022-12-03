import abc
from src.shared.helpers.errors.domain_errors import TypeError
from src.shared.helpers.errors.domain_errors import EntityError

class Table(abc.ABC):
    tableNumber: int
    numberOfPeople: int
    
    def __init__(self, tableNumber: int, numberOfPeople: int):
        if type(tableNumber) != int:
            raise TypeError('tableNumber', 'int')
        if type(numberOfPeople) != int:
            raise TypeError('numberOfPeople', 'int')
        if numberOfPeople <= 0:
            raise EntityError('numberOfPeople')
        self.tableNumber = tableNumber
        self.numberOfPeople = numberOfPeople