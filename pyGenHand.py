#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Tue Jul 12 01:16:40 2022 CDT
# Last ModDate: Tue Jul 12 16:12:14 2022 CDT
# =============================================================================
# Notes:
# =============================================================================

from random import choice
from random import shuffle
from random import randrange
from itertools import product
from collections import defaultdict
from copy import deepcopy # https://stackoverflow.com/a/2465951/1896134

# print(u"\u2666") # diamond ♦
# print(u"\u2665") # heart ♥
# print(u"\u2663") # club ♣
# print(u"\u2660") # spade ♠

class Poker(object):
    def __init__(self):
        self.Suit = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
        self.SuitLen = len(self.Suit)
        self.Card = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.Card = [x.rjust(2) for x in self.Card]
        self.CardLen = len(self.Card)
        self.Suit = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
        self.FullDeck = defaultdict()
        self.FullDeck = list(product(tuple(self.Card), tuple(self.Suit)))
        self.FullDeck = dict((i,j) for i,j in enumerate(self.FullDeck))

    def dealHand(self, NumberOfCards):
        self.HandDealt = []
        self.UpdatedDeck = deepcopy(self.FullDeck)
        try:
            for i in range(NumberOfCards):
                self.Key, self.Value = choice(list(self.UpdatedDeck.items()))
                if self.Value not in self.HandDealt:
                    self.HandDealt.append(self.Value)
                    del self.UpdatedDeck[self.Key]
        except IndexError as e:
            print('Ran out of cards to deal You have the Whole Deck Listed.')
        print(f"Hand Dealt: {self.HandDealt}")

if __name__ == '__main__':
    a = Poker()
    a.dealHand(2)
    a.dealHand(3)
    a.dealHand(4)
    a.dealHand(5)
