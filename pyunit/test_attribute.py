import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from models.attribute import Attribute

@pytest.mark.parametrize("add_label, add_value, expected_add_label, expected_add_value", [
    (20, 20, 21, 19),
    ("20", "20", 21, 19),
    (0, 0, 0, 0),
    (-1, -1, -1, -1),
    (1, 0, 1, 0),
    (0, 1, 1, 0)
])
def test_addattribute(add_label, add_value, expected_add_label, expected_add_value):
    result = Attribute().add(add_label, add_value)
    assert result == (expected_add_label,expected_add_value)

@pytest.mark.parametrize("reduce_label, reduce_value, expected_reduce_label, expected_reduce_value", [
    (20, 20, 19, 21),
    ("20", "20", 19, 21),
    (0, 0, 0, 0),
    (-1, -1, -1, -1),
    (1, 0, 1, 0),
    (2, 0, 1, 1),
    (0, 1, 0, 1)
])
def test_reduceattribute(reduce_label, reduce_value, expected_reduce_label, expected_reduce_value):
    result = Attribute().reduce(reduce_label, reduce_value)
    assert result == (expected_reduce_label,expected_reduce_value)

@pytest.mark.parametrize("dicevalue, useratr,expected", [
    (20, [[1,"DreamHolo",18]],38),
    ("20", [[1,"DreamHolo",18]],38),
    (0, [[1,"DreamHolo",18]],18),
    (-1, [[1,"DreamHolo",18]],17),
    (1, [[1,"DreamHolo",18]],1),
    (0, [[1,"DreamHolo",18]],18)
])
def test_getattribute(dicevalue,useratr,expected):
    result = Attribute().getattribute(dicevalue, useratr)
    assert result == expected