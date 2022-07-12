#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 11 12:46:00 PDT 2022
# Last ModDate: Tue Jul 12 16:12:14 2022 CDT
# =============================================================================
# Notes:
# =============================================================================

from random import randrange

def GenerateRandomRGB():
    f"""Generate Random RGB Tuple: (000,000,000) to (255, 255, 255)."""
    randomRGB = [0]*3                   # A list variable to hold empty list.
    i = 0                               # Declare and set loop counter to 0.
    for i in range (0,3):               # Loop Three Times
        randomRGB[i] = randrange(0,256) # Choose A Random Number Between 0 & 255
    return tuple(randomRGB)

if __name__ == '__main__':
    a = GenerateRandomRGB()
    print(f"Your Random RGB Color is: {a}  'GenerateRandomRGB()'")
    print(f"R: {a[0]}")
    print(f"G: {a[1]}")
    print(f"B: {a[2]}")
