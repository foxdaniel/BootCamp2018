# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 08:55:29 2018

@author: danie
"""
import unittest as ut
import pytest

# Problem 1

def test_smallest_factor():
    assert ut.smallest_factor(1) == 1, "Failed"
    assert ut.smallest_factor(4) == 2, "Failed"
    assert ut.smallest_factor(6) == 2, "Failed"
    assert ut.smallest_factor(5) == 5, "Failed"
    assert ut.smallest_factor(8) == 2, "Failed"
    assert ut.smallest_factor(9) == 3, "Failed"
    

# Problem 2
    
def test_month_length():
    assert ut.month_length("September") == 30, "30 months fail"
    assert ut.month_length("January") == 31, "31rd months fail"
    assert ut.month_length("daniel") == None, "None months fail"
    assert ut.month_length("February", leap_year=True) == 29, "Feb, leapyr fails"
    assert ut.month_length("February", leap_year=False) == 28, "Feb, nonleapyr fails"
    

# Problem 3

def test_operate():
    with pytest.raises(TypeError) as excinfo:
        ut.operate(0, 0, 0)
    assert ut.operate(1, 2, '+') == 3, "addition"
    assert ut.operate(3, 2, '-') == 1, "subtraction"
    assert ut.operate(1, 2, '*') == 2, "multiplication"
    assert ut.operate(4, 2, '/') == 2, "division"

    with pytest.raises(TypeError) as excinfo:
        ut.operate(1, 2, 3)
    with pytest.raises(ZeroDivisionError) as excinfo:
        ut.operate(1, 0, '/')
    with pytest.raises(ValueError) as excinfo:
        ut.operate(1, 0, 'y')
        

# Problem 4
        
@pytest.fixture
def set_up_fractions():
    frac_1_2 = ut.Fraction(1, 2)
    frac_2_3 = ut.Fraction(2, 3)
    frac_n2_3 = ut.Fraction(-2, 3)
    frac_1_4 = ut.Fraction(1, 4)
    frac_0_1 = ut.Fraction(0, 1)
    return frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1

def test_fraction_init(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert frac_1_2.denom == 2
    assert frac_2_3.numer == 2
    assert frac_n2_3.numer == -2
    frac = ut.Fraction(26, 40) # 13/20.
    assert frac.numer == 13
    assert frac.denom == 20

    with pytest.raises(ZeroDivisionError) as excinfo:
        ut.Fraction.__init__('Test', 7, 0)
    with pytest.raises(TypeError) as excinfo:
        ut.Fraction.__init__('Test', 3.5, 2)

def test_fraction_str(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert str(frac_1_2) == "1/2"
    assert str(frac_2_3) == "2/3"
    assert str(frac_n2_3) == "-2/3"
    assert str(frac_1_4) == "1/4"

def test_fraction_float(set_up_fractions):
    frac_1_2, frac_1_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert float(frac_1_2) == .5
    assert float(frac_2_3) == 2 / 3.
    assert float(frac_n2_3) == -2 / 3.
    assert float(frac_1_4) == .25

def test_fraction_eq(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert frac_1_2 == ut.Fraction(1, 2)
    assert frac_2_3 == ut.Fraction(4, 6)
    assert frac_n2_3 == ut.Fraction(8, -12)
    assert frac_1_4 == ut.Fractions(4, 16)
    assert float(frac_n2_3) == frac_n2_3

def test_fraction_add(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert frac_2_3 + frac_1_4 == ut.Fraction(11, 12)

def test_fraction_sub(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert frac_2_3 - frac_1_4 == ut.Fraction(5, 12)

def test_fraction_mul(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert frac_2_3 * frac_1_4 == ut.Fraction(1, 6)

def test_fraction_div(set_up_fractions):
    frac_1_2, frac_2_3, frac_n2_3, frac_1_4, frac_0_1 = set_up_fractions
    assert frac_2_3 / frac_1_4 == ut.Fraction(8, 3)
    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_2_3 / frac_0_1

# Problem 5 and 6
        
@pytest.fixture
def set_up_hands():
    hand1 = ["1022", "1122", "0100", "2021", "0010", "2201",
             "2111", "0020", "1102", "0210", "2110", "1020"]
    bad_amount = ["0000"]
    not_unique = ["0000", "0000", "0000", "0000", "0000", "0000",
                     "0000", "0000", "0000", "0000", "0000", "0000"]
    wrong_digit = ["00000", "1122", "0100", "2021", "0010", "2201",
                       "2111", "0020", "1102", "0210", "2110", "1020"]
    wrong_charac = ["3022", "1122", "0100", "2021", "0010", "2201",
                     "2111", "0020", "1102", "0210", "2110", "1020"]
    return hand1, bad_amount, not_unique, wrong_digit, wrong_charac

def test_count_sets():
    hand1, bad_amount, not_unique, wrong_digit, wrong_charac = set_up_hands()
    assert ut.count_sets(hand1) == 6
    with pytest.raises(ValueError) as excinfo:
        ut.count_sets(bad_amount)
    with pytest.raises(ValueError) as excinfo:
        ut.count_sets(not_unique)
    with pytest.raises(ValueError) as excinfo:
        ut.count_sets(wrong_digit)
    with pytest.raises(ValueError) as excinfo:
        ut.count_sets(wrong_charac)

def test_is_set():
    # Different in all aspects
    assert ut.is_set("0000", "1111", "2222") == True
    assert ut.is_set("1022", "1122", "1020") == False
    assert ut.is_set("1020", "1120", "1220") == True