import sys
import os
import random as random
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.dice import Dice

@pytest.mark.parametrize("iteration", range(100))
def test_pulldice(iteration):
    result = Dice(random).pulldice()
    assert 1 <= result <= 20

@pytest.mark.parametrize("dice, addatr,expected", [
    (20, 10, [30,"Выпало значение: 20 Критический успех"]),
    ("20", 15, [35,"Выпало значение: 20 Критический успех"]),
    (0, 20, [20,"Выпало значение: 0"]),
    (-1, 5, [4,"Выпало значение: -1"]),
    (1, 4, [1,'Выпало значение: 1 Критический провал']),
    (0, -3, [-3,'Выпало значение: 0'])
])
def test_diceresult(dice,addatr,expected):
    result = Dice(random).diceresult(dice, addatr)
    result == expected