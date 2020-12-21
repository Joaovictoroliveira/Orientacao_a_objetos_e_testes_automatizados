import pytest

def concat_name(first, last):
    name = last + ', ' + first
    return name

def test_answer():
    assert(concat_name("John", "Doe")) == "Doe, John"
