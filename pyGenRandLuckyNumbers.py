#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.9.5 ('v3.9.5:0a7dcbdb13', 'May  3 2021 13:17:02')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 11 12:46:00 2022 PDT
# Last ModDate: Wed Jun 22 11:02:29 2022 CDT
# =============================================================================
# Notes:
# =============================================================================

from random import randrange


def generateLuckyNumbers():
    lotteryNumbers = [0]*6  # A list variable to hold empty list.
    i = 0  # Declare and set loop counter to 0.
    for i in range (0,6):
        lotteryNumbers[i] = randrange(0,60)
        lotteryNumbers[i] = f"{lotteryNumbers[i]:02d}"
    str1 = ', '.join(e for e in lotteryNumbers)
    return str1, lotteryNumbers

if __name__ == '__main__':
    print(f"Your Luck Numbers For Today Are: {generateLuckyNumbers()[0]}")
