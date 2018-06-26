# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 08:19:00 2018

@author: danie
"""

import box
import sys
import numpy as np
import random
import time

# Be sure to have the  correct order of
# command line arguments: file name, player's name, time limits

# If 3 command line arguments are given properly, start the game
if len(sys.argv) == 3:

    # player name
    name = sys.argv[1]
    # time limit
    time_lim = float(sys.argv[2]) # time limit (sec)
    remaining = list(np.arange(9)+1)

    remaining_time = time_lim

    while remaining_time > 0:
        start_time = time.time()
        sum_remaining = sum(remaining)
        roll1 = np.random.randint(1,6)
        if sum_remaining <= 6:
            roll2 = 0
        else:
            roll2 = np.random.randint(1,6)
        sum_rolls = roll1 + roll2

        end_time = time.time()
        loop_time = end_time - start_time
        remaining_time -= loop_time

        
        print("\nNumbers flushleft: " + str(remaining)
              + "\nRoll : " + str(sum_rolls)
              + "\nSeconds left " + str(round(remaining_time, 2)))

       
        isvalidRoll = box.isvalid(sum_rolls, remaining)

        if not isvalidRoll:
            print("\nScore for player " + name + ": 0 points")
            print("Time played: " + str(round((time_lim - remaining_time), 2)) + " seconds.")
            print('You lost, ' + name + ".")
            break

        true_input = False
        while not true_input:

            start_time = time.time()

            input_values = input("Numbers to eliminate: ")
            choices = box.parse_input(input_values, remaining)
            if choices != []:
                if sum(choices) == sum_rolls:
                    true_input = True
                    break
            print("Invalid input. Try again.")

            end_time = time.time()
            loop_time = end_time - start_time
            remaining_time -= loop_time

            print("\nSeconds left " + str(round(remaining_time, 2)))

        for x in choices:
            remaining.remove(x)

        end_time = time.time()
        loop_time = end_time - start_time
        remaining_time -= loop_time

        if remaining_time < 0:
            print("\nScore for player " + name + ": 0 points")
            print("You ran out of time and lost, " + name + "!")
            print("Time played: " + str(round((time_lim - remaining_time), 2)) + " seconds.")
            break

        if not remaining:
            print("\nScore for player " + name + ": 1 point")
            print('You won, ' + name + "!")
            print("Time played: " + str(round((time_lim- remaining_time), 2)) + " seconds.")
# the game will not start unless 3 commandline arguments are provided
else:
    print("Need exactly three command line arguments to play the game.")