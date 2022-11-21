import abc

class Table(abc.ABC):
    tableNumber: int
    numberOfPeople: int
    
    def __init__(self, tableNumber: int, numberOfPeople: int):
        if type(tableNumber) != int:
            raise TypeError("tableNumber must be int")
        if type(numberOfPeople) != int:
            raise TypeError("numberOfPeople must be int")
        self.tableNumber = tableNumber
        self.numberOfPeople = numberOfPeople