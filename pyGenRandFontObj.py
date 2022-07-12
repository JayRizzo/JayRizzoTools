#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Wed Jun 29 20:00:35 2022 CDT
# Last ModDate: Tue Jul 12 16:47:08 2022 CDT
# =============================================================================
# Notes: Get a listing of all known fonts from your mac.
# =============================================================================

import glob
from getpass import getuser
from os.path import exists as filepathexist
from os.path import expanduser
from os.path import join
from random import choice

FontPath = ''
FontList = []
GLOBList = []

def getFontList():
    """Compile a list of all known fonts on the MacOS into a list.
    """
    FontPath = r'/System/Library/Fonts/Supplemental'
    exists = filepathexist(FontPath)
    if exists:
        FontPath = fr'{FontPath}/*.*'
        List_GLOB = glob.glob(FontPath)
        FontList.extend(List_GLOB)
    FontPath = r'/Library/Fonts'
    exists = filepathexist(FontPath)
    if exists:
        FontPath = fr'{FontPath}/*.*'
        List_GLOB = glob.glob(FontPath)
        FontList.extend(List_GLOB)
    FontPath = r'/System/Library/Fonts'
    exists = filepathexist(FontPath)
    if exists:
        FontPath = fr'{FontPath}/*.*'
        List_GLOB = glob.glob(FontPath)
        FontList.extend(List_GLOB)
    FontPath = fr'/Users/{getuser()}/Library/Fonts'
    exists = filepathexist(FontPath)
    if exists:
        FontPath = fr'{FontPath}/*.*'
        List_GLOB = glob.glob(FontPath)
        FontList.extend(List_GLOB)
        FontList.sort()
    FontList.remove('/System/Library/Fonts/Apple Color Emoji.ttc')  # Removed for Breaking when used by PIL.
    return FontList


if __name__ == '__main__':
    a = choice(getFontList())
    FontNameStr = a.split('/')[-1].split('.')[0]
    print(f"Your Random Font: {FontNameStr}\tPath: {a}")
    for i in sorted(getFontList()):
        FontNameStr = i.split('/')[-1].split('.')[0]
        print(f"CurrentFontName: {FontNameStr}: {i}")
