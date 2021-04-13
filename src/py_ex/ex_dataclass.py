from dataclasses import dataclass
from dataclasses import field

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

@dataclass(order=True,unsafe_hash=True)
class Person:
    """Listing of person name and zip code
    This object allows for adding to a dictionary
    by using the 'unsafe_hash' option. 
    """
    name: str
    zip: int

@dataclass()
class FavoriteThings:
    '''
    Listing my favorite things
    '''
    mylist: list = field(default_factory=list)