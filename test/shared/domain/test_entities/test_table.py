import pytest

from src.shared.domain.entities.table import Table
from src.shared.helpers.errors.domain_errors import TypeError
from src.shared.helpers.errors.domain_errors import EntityError


class Test_table():
    def test_table(self):
        table = Table(tableNumber=1, numberOfPeople=2)
        
        assert table.tableNumber == 1
        assert table.numberOfPeople == 2
    
    def test_table_tableNumber_must_be_int(self):
        with pytest.raises(TypeError):
            Table(tableNumber='Um', numberOfPeople=2)
    
    def test_table_numberOfPeople_must_be_int(self):
        with pytest.raises(TypeError):
            table = Table(numberOfPeople='Um', tableNumber=1)
            
    def test_table_numberOfPeople_must_be_greater_than_zero(self):
        with pytest.raises(EntityError):
            table = Table(numberOfPeople=0, tableNumber=1)
    