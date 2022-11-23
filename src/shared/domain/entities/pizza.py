import abc
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER
from src.shared.helpers.errors.domain_errors import TypeError

class Pizza(abc.ABC):
    flavor: FLAVOR
    border: BORDER
    
    def __init__(self, flavor: FLAVOR, border: BORDER = None):
        if border == None:
            border = BORDER.NONE
        if type(flavor) != FLAVOR:
            raise TypeError('flavor', 'ENUM.FLAVOR')
        if type(border) != BORDER:
            raise TypeError('border', 'ENUM.BORDER')
        self.flavor = flavor
        self.border = border