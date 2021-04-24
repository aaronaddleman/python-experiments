from py_ex.ex_dataclass import *

import pytest

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

@pytest.fixture
def mythings_noparams():
    return FavoriteThings()

def test_inventory_list(inventory_items):
    assert 2 == len(inventory_items)
    assert 'apple' == inventory_items[0].name
    assert 'pear' != inventory_items[0].name

def test_people_dict(people_dict):
    '''
    lets see what we can do with just dictionaries
    '''
    assert 4 == len(people_dict)

def test_mythings_noparams(mythings_noparams):
    '''
    What do you get with no favorite things?
    Notice there are no params being passed..
    also.. the example in the docs says to use
    mylist: list[int]
    and that is incorrect...
    '''
    assert FavoriteThings(mylist=[]) == mythings_noparams
    mythings_noparams.mylist += [4,5,6]
    assert 3 == len(mythings_noparams.mylist)