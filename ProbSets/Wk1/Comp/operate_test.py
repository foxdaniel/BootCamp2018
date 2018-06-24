# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:55:20 2018

@author: danie
"""

import pytest
import operate as op
def test_operate():
    assert op.operate(1, 2, '+') == 3, "addition"
    assert op.operate(3, 2, '-') == 1, "subtraction"
    assert op.operate(1, 2, '*') == 2, "addition"
    assert op.operate(4, 2, '/') == 2, "addition"

    with pytest.raises(TypeError) as excinfo:
        op.operate(1, 2, 3)
    with pytest.raises(ZeroDivisionError) as excinfo:
        op.operate(1, 0, '/')
    with pytest.raises(ValueError) as excinfo:
        op.operate(1, 0, 'y')
    pass