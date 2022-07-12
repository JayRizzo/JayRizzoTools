#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 02:25:47 2022 CDT
# Last ModDate: Tue Jul 12 16:14:33 2022 CDT
# =============================================================================
# Notes:
# =============================================================================

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ListInsideOfListError(Error):
    """Error: This List Contains Another list Please Fix the list & try again!
    https://www.programiz.com/python-programming/user-defined-exception
    """
    pass


class ListChecker(object):
    def __init__(self):
        self.x = None
        self.el = []

    def main(self, x: list):
        super(ListChecker, self).__init__()
        self.el = x
        try:
            self.x = any(isinstance(el, list) for el in x)
            if self.x is True:
                raise ListInsideOfListError
                return self.x, self.el
            else:
                return self.x, self.el
        except ListInsideOfListError:
            a = ListInsideOfListError(f"({self.x}, {self.el}, ERROR: This List Contains Another list Please Fix the list & try again!)")
        raise(a)


if __name__ == '__main__':
    print("""Examples are as follows:
    bb = ['test', 'consolidated list should return True']
    f = ListChecker().main(bb)
    print(f"{f}")
    # Returns: (False, ['test', 'consolidated list should return True'])
    try:
        aa = ['test', ['another list should return False']]
        d = ListChecker().main(aa)
        print(d)
    except Exception as e:
        print(f"{e}")
        # Returns: (True, ['test', ['another list should return False']], ERROR: This List Contains Another list Please Fix the list & try again!)
        exit()
""")
    bb = ['test', 'consolidated list should return True']
    f = ListChecker().main(bb)
    print(f"{f}")
    # Returns: (False, ['test', 'consolidated list should return True'])
    try:
        aa = ['test', ['another list should return False']]
        d = ListChecker().main(aa)
        print(d)
    except Exception as e:
        print(f"{e}")
        # Returns: (True, ['test', ['another list should return False']], This List Contains Another list Please Fix the list & try again!)
        exit()

