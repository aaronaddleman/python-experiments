import pytest
from dataThings import *

@pytest.fixture
def inventory_items():
    return [
        InventoryItem(name='apple', unit_price=1.00, quantity_on_hand=7),
        InventoryItem(name='oranges', unit_price=0.50, quantity_on_hand=3)
    ]

@pytest.fixture
def people_dict():
    return [
        Person(name='Ringo', zip=11111),
        Person(name='Paul', zip=22222), 
        Person(name='George', zip=33333),
        Person(name='John', zip=44444)
    ]

def test_inventory_list(inventory_items):
    assert 2 == len(inventory_items)
    assert 'apple' == inventory_items[0].name
    assert 'pear' != inventory_items[0].name

def test_people_dict(people_dict):
    '''
    lets see what we can do with just dictionaries
    '''
    assert 4 == len(people_dict)

