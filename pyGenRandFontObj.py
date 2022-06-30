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
    """Compile list of all known fonts on the MacOS into a list.
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
    FontList.remove('/System/Library/Fonts/Apple Color Emoji.ttc')  # Removed for Breaking when used by PIL.
    return FontList


if __name__ == '__main__':
    a = choice(getFontList())
    FontNameStr = a.split('/')[-1].split('.')[0]
    print(f"Your Random Font: {FontNameStr}\tPath: {a}")
    # for i in sorted(getFontList()):
    #     FontNameStr = i.split('/')[-1].split('.')[0]
    #     print(f"CurrentFontName: {FontNameStr}: {i}")