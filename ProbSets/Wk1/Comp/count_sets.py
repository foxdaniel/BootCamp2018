# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:19:07 2018

@author: danie
"""

import itertools as it
import numpy as np
def count_sets(cards):
    """Return the number of sets in the provided Set hand.
     Parameters:
         cards (list(str)) a list of twelve cards as 4-bit integers in
         base 3 as strings, such as ["1022", "1122", ..., "1020"].
     Returns:
         (int) The number of sets in the hand.
     Raises:
         ValueError: if the list does not contain a valid Set hand, meaning
             - there are not exactly 12 cards,
             - the cards are not all unique,
             - one or more cards does not have exactly 4 digits, or
             - one or more cards has a character other than 0, 1, or 2.
    """

    if len(cards) != 12:
        raise ValueError("there are not exactly 12 cards")
    setofcards = set(cards)
    if len(setofcards) != 12:
        raise ValueError("the cards are not all unique")
    for i in cards:
        if len(i) != 4:
            raise ValueError("one or more cards does not have exactly 4 digits")
        for j in i:
            if j == '0' or j == '1' or j == '2':
                pass
            else:
                raise ValueError("one or more cards has a character other than 0, 1, or 2")
    poss_sets = list(it.combinations(cards, 3))
    poss_sets_len = len(poss_sets)
    poss_sets_vec = np.zeros(poss_sets_len)
    for i, val in enumerate(poss_sets):
        if is_set(*val):
            poss_sets_vec[i] = 1
    return int(sum(poss_sets_vec))


def is_set(a, b, c):
    """Determine if the cards a, b, and c constitute a set.
     Parameters:
         a, b, c (str): string representations of 4-bit integers in base 3.
             For example, "1022", "1122", and "1020" (which is not a set).
     Returns:
         True if a, b, and c form a set, meaning the ith digit of a, b,
             and c are either the same or all different for i=1,2,3,4.
         False if a, b, and c do not form a set.
    """

    set1 = {a[0], b[0], c[0]}
    set2 = {a[1], b[1], c[1]}
    set3 = {a[2], b[2], c[2]}
    set4 = {a[3], b[3], c[3]}
    digit1 = (len(set1) == 1 or len(set1) == 3)
    digit2 = (len(set2) == 1 or len(set2) == 3)
    digit3 = (len(set3) == 1 or len(set3) == 3)
    digit4 = (len(set4) == 1 or len(set4) == 3)
    if digit1 == True and digit2 == True and digit3 == True and digit4 == True:
        return True
    else:
        return False
a = "1022"
b = "2021"
c = "0020"
d = "1023"
is_set(a, b, c)
hand1 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "1020"]
count_sets(hand1)