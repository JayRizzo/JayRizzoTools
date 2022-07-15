#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 11 12:46:00 2022 PDT
# Last ModDate: Tue Jul 12 16:48:57 2022 CDT
# =============================================================================
# Notes:
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

def generateEmojiHEX():
    randomHEX = [0]*8  # A list variable to hold empty list.
    i = 0  # Declare and set loop counter to 0.
    for i in range (0,8):
        randomHEX[i] = choice(hexdigits[0:16])
    str1 = ''.join(str(e) for e in randomHEX)
    str1 = f"\'\\U{str1}\'"
    return f"{str1}"

if __name__ == '__main__':
    print(f"Your Random HEX Color is: {generateRandomHEX()}")
    print(f"Your Random HEX Emoji is: {generateEmojiHEX()}")

