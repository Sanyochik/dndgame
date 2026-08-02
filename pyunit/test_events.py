import sys
import os
import random as random
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.db import DB
from models.users import Users
from models.events import Events

@pytest.mark.parametrize("iteration", range(100))
def test_pulldice(iteration):
    result = Events(DB, random, Users).pulldice()
    assert 1 <= result <= 20
@pytest.mark.parametrize("dicevalue, useratr,expected", [
    (20, [[1,"DreamHolo",18]],38),
    ("20", [[1,"DreamHolo",18]],38),
    (0, [[1,"DreamHolo",18]],18),
    (-1, [[1,"DreamHolo",18]],17),
    (1, [[1,"DreamHolo",18]],1),
    (0, [[1,"DreamHolo",18]],18)
])
def test_addattribute(dicevalue,useratr,expected):
    result = Events(DB, random, Users).getattribute(dicevalue, useratr)
    result == expected

@pytest.mark.parametrize("dice, addatr,expected", [
    (20, 10, [30,"Выпало значение: 20 Критический успех"]),
    ("20", 15, [35,"Выпало значение: 20 Критический успех"]),
    (0, 20, [20,"Выпало значение: 0"]),
    (-1, 5, [4,"Выпало значение: -1"]),
    (1, 4, [1,'Выпало значение: 1 Критический провал']),
    (0, -3, [-3,'Выпало значение: 0'])
])
def test_diceresult(dice,addatr,expected):
    result = Events(DB, random, Users).diceresult(dice, addatr)
    result == expected