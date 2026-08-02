import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from models import attribute

@pytest.mark.parametrize("add_label, add_value, expected_add_label, expected_add_value", [
    (20, 20, 21, 19),
    ("20", "20", 21, 19),
    (0, 0, 0, 0),
    (-1, -1, -1, -1),
    (1, 0, 1, 0),
    (0, 1, 1, 0)
])
def test_addattribute(add_label, add_value, expected_add_label, expected_add_value):
    result = attribute.add(add_label, add_value)
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
    result = attribute.reduce(reduce_label, reduce_value)
    assert result == (expected_reduce_label,expected_reduce_value)