import abc
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.borda_enum import BORDA
from src.shared.helpers.errors.domain_errors import TypeError

class Pizza(abc.ABC):
    flavor: FLAVOR
    borda: BORDA
    
    def __init__(self, flavor: FLAVOR, borda: BORDA = None):
        if borda == None:
            borda == BORDA.NONE
        if type(flavor) != FLAVOR:
            raise TypeError('flavor', 'FLAVOR')
        if type(borda) != BORDA:
            raise TypeError('borda', 'BORDA')
        self.flavor = flavor
        self.borda = borda