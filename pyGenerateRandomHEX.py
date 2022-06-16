#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 11 12:46:00 PDT 2022
# =============================================================================
from random import choice
from string import hexdigits

def generateRandomHEX():
    randomHEX = [0]*6  # A list variable to hold empty list.
    i = 0  # Declare and set loop counter to 0.
    for i in range (0,6):
        randomHEX[i] = choice(hexdigits[0:16])
    str1 = ''.join(str(e) for e in randomHEX)
    return f"{str1}"

if __name__ == '__main__':
    print(f"Your Random HEX Color is: {generateRandomHEX()}")
