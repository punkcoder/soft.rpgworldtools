from src.util import roller


def test_roller_1d4():
    for i in range(1,100):
        roll = roller.Roll("1d4") 
        assert roll["result"] >= 1
        assert roll["result"] <= 4

def test_roller_1d6():
    for i in range(1,100):
        roll = roller.Roll("1d6") 
        assert roll["result"] >= 1
        assert roll["result"] <= 6

def test_roller_2d6():
    for i in range(1,100):
        roll = roller.Roll("2d6") 
        assert roll["result"] >= 2
        assert roll["result"] <= 12

def test_roller_3d8():
    for i in range(1,100):
        roll = roller.Roll("3d8") 
        assert roll["result"] >= 2
        assert roll["result"] <= 24

def test_roller_1d4_add_1():
    for i in range(1,100):
        roll = roller.Roll("1d4+1") 
        assert roll["result"] >= 2
        assert roll["result"] <= 5


def test_roller_1d4_sub_1():
    for i in range(1,100):
        roll = roller.Roll("1d4-1") 
        assert roll["result"] >= 0
        assert roll["result"] <= 3


def test_roller_4d6drop1():
    for i in range(1,100):
        roll = roller.Roll("4d6(3)") 
        assert roll["result"] >= 3
        assert roll["result"] <= 18