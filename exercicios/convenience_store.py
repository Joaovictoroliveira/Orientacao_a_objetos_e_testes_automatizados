import pytest

def change_enough(change, amount_due):
    resp = ((change[0] * 0.25) + (change[1] * 0.10) + (change[2] * 0.05 + (change[3] * 0.01)))

    if resp >= amount_due:
        return True
    else:
        return False

def test_answer():
    assert(change_enough([30, 40, 20, 5], 12.55)) == True
