from dataclasses import dataclass

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
    """Listing of person name and zip code"""
    name: str
    zip: int
