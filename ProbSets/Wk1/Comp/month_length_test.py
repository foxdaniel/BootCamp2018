# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:40:49 2018

@author: danie
"""

# Problem 2

import monthlength as ml

def test_month_length():
    assert ml.month_length("September") == 30, "30 months fail"
    assert ml.month_length("January") == 31, "31rd months fail"
    assert ml.month_length("cache") == None, "None months fail"
    assert ml.month_length("February", leap_year=True) == 29, "Feb, leapyr fails"
    assert ml.month_length("February", leap_year=False) == 28, "Feb, nonleapyr fails"
    pass