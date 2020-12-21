import pytest

def is_empty(string):
    if string == "":
        return True
    return False

def test_answer_True():
    assert is_empty("") == True

test_answer_True()
