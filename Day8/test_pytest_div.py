'''
Day 8
PyTest
'''
import pytest
from div import floordiv

def test_div_asserts_proper_value():
    assert floordiv(4,2) == 2

def test_div_asserts_zero():
    assert floordiv(2,4) == 0

def test_div_asserts_integer_and_not_float():
    assert floordiv(10,3) == 3

def test_div_asserts_one():
    assert floordiv(3,3) == 1