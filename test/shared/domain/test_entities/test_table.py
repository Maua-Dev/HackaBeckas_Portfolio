import pytest

from shared.helpers.errors.domain_errors import EntityError
from shared.domain.entities.table import Table

class Test_table():
    def test_table(self):
        table = Table(tableNumber=1, numberOfPeople=2)
        
        assert table == Table(tableNumber=1, numberOfPeople=2)
    
    def test_table_tableNumber_must_be_int(self):
        with pytest.raises(EntityError):
            table = Table(tableNumber='Um')