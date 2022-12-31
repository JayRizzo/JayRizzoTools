# JayRizzoTools
Aggregation of Scripts to make life a bit more interesting.

# Python
## [pyGenHand.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyTubeGUI.py)
* Download Any Youtube Video to an Audio or Video File Format.
* Automatically Creates And Download Into These Folders
  - Audio Files In MUSIC FOLDER: ~/Music/JayRizzoDL
  - Video Files In Movies FOLDER: ~/Movies/JayRizzoDL

```bash
python3 pyTubeGUI.py
```
![20221231_121403](https://user-images.githubusercontent.com/22861678/210152312-600b4797-d396-4697-866d-d7620a0bdc62.png)

# Python
## [pyGenHand.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenHand.py)
* Generate a Random Hand of x# of cards. (poker, blackjack)

```python3
import pyGenHand

a = pyGenHand.Poker()
a.dealHand(5)

# Returns: 
Hand Dealt: [(' A', '♠'), ('10', '♥'), (' 9', '♣'), (' 3', '♥'), (' J', '♦')]
```

## [pyGenRand256Color.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRand256Color.py)
* Generate a Random String containing information of the Standard 256 colors.

```python3
from random import choice
import pyGenRand256Color


a = pyGenRand256Color
b = dict(choice(a.two56colors))
print(b['colorId'])
print(b['name'])
print(b['hexString'])
print(b['rgb'])
print(b['hsl'])

# Returns:
24
DeepSkyBlue4
#005f87
{'r': 0, 'g': 95, 'b': 135}
{'h': 197.777777777778, 's': 100, 'l': 26}
```

## [pyGenRandAdjective.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandAdjective.py)
* Generate a Random String containing an Adjective.

```python3
from random import choice
import pyGenRandAdjective

a = pyGenRandAdjective
b = choice(a.adjectives)
print(b)

# Returns:
Tender-Hearted
```

## [pyGenRandAdverb.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandAdverb.py)
* Generate a Random String containing an Adverb.

```python3
from random import choice
import pyGenRandAdverb

a = pyGenRandAdverb
b = choice(a.adverbs)
print(b)

# Returns:
Utterly
```

## [pyGenRandAnimal.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandAnimal.py)
* Generate a Random String containing an Animal.

```python3
from random import choice
import pyGenRandAnimal

a = pyGenRandAnimal
b = choice(a.animals)
print(b)

# Returns:
Flamingo
```

## [pyGenRandCompanieName.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandCompanieName.py)
* Generate a Random String containing a random company name.

```python3
from random import choice
import pyGenRandCompanieName

a = pyGenRandCompanieName
b = choice(a.companies)
print(b)

# Returns:
American Electric Power
```

## [pyGenRandEmoji.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandEmoji.py)
* Generate a Random String containing a random Emoji Character.

```python3
from random import choice
import unicodedata
import pyGenRandEmoji
from pyGenRandEmoji import emojis

emoji = choice(emojis)
begwrap = "{"
endwrap = "}"
# https://docs.python.org/3/howto/unicode.html?highlight=unicode%20howto#the-string-type
# https://unicode.org/emoji/charts-13.0/emoji-released.html
# NOTE: Sometimes throws an error "No such name"  https://stackoverflow.com/a/24553272/1896134
print(f"Emoji:\t\t\t\t{ascii(emoji)}")
print(f"HEX:\t\t\t\t{emoji.encode('UTF-8')}")
print(f"Unicode Name:\t\t'\\N{begwrap}{unicodedata.name(emoji)}{endwrap}'")
print(f"Returns:\t\t\t{emoji}")

# Returns:
Emoji:              '\U0001f63a'
HEX:                b'\xf0\x9f\x98\xba'  
Unicode Name:       '\N{SMILING CAT FACE WITH OPEN MOUTH}'
Returns:            😺

# Checking: 
print('\U0001f63a')
print(bytes(b'\xf0\x9f\x98\xba').decode('utf-8'))
print('\N{SMILING CAT FACE WITH OPEN MOUTH}')
# All Return the expected emoji:
'😺'
```

## [pyGenRandFontObj.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandFontObj.py)
* Generate a Random String containing a random Font from your Mac Machine.

```python3
from random import choice
import pyGenRandFontObj

a = choice(pyGenRandFontObj.getFontList())
FontNameStr = a.split('/')[-1].split('.')[0]
print(f"Your Random Font: {FontNameStr}\tPath: {a}")

# Results:
Your Random Font: Khula-SemiBold    Path: ~/Library/Fonts/Khula-SemiBold.ttf

# OR if you want to know every font you have
# Minus one ('/System/Library/Fonts/Apple Color Emoji.ttc')  Removed for Breaking when used by PIL.

for i in sorted(pyGenRandFontObj.getFontList()):
    FontNameStr = i.split('/')[-1].split('.')[0]
    print(f"CurrentFontName: {FontNameStr}: {i}")

# Results:
CurrentFontName: Arial Unicode: /Library/Fonts/Arial Unicode.ttf
... (list all fonts)
CurrentFontName: ubuntu: ~/Library/Fonts/ubuntu.ttf
```

## [pyGenRandLuckyNumbers.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandLuckyNumbers.py)
* Generate a Random Tuple containing a random set of 6 numbers.

```python3
from pyGenRandLuckyNumbers import generateLuckyNumbers

a = generateLuckyNumbers()[0]  # Returns Comma separated string
print(a)

b = generateLuckyNumbers()[1]  # Returns [LIST]
print(b)

c = generateLuckyNumbers()     # Returns tuple(Comma separated string & [LIST])
print(c)

# Results Respectively for each print statement as Follows:
07, 00, 49, 13, 23, 37
['32', '13', '33', '22', '16', '53']
('48, 21, 40, 46, 43, 13', ['48', '21', '40', '46', '43', '13'])
```

## [pyGenRandHEX.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandHEX.py)
* Generate a Random String containing a random HEX.

```python3
from pyGenRandHEX import GenerateRandomHEX

a = GenerateRandomHEX()
print(f"Your Random HEX Color is: {a}  'GenerateRandomHEX()'")

# Results Respectively for each print statement as Follows:
Your Random HEX Color is: e4ad64
```

## [pyGenRandRGB.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandRGB.py)
* Generate a Random Tuple containing a random set of 6 numbers.

```python3
from pyGenRandRGB import GenerateRandomRGB

a = GenerateRandomRGB()
print(f"Your Random RGB Color is: {a}  'GenerateRandomRGB()'")
print(f"R: {a[0]}")
print(f"G: {a[1]}")
print(f"B: {a[2]}")

# Results Respectively for each print statement as Follows:
Your Random RGB Color is: (62, 38, 216)  'GenerateRandomRGB()'
R: 62
G: 38
B: 216
```

## [pyGenRandStatement.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandStatement.py)
* Generate a Random String containing a random phrase.

```bash
python3 pyGenRandStatement.py

# Do Not Lie
```

## [pyGetSystemUpTime.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGetSystemUpTime.py)
* Generate your system uptime in a readable format from epoch time.

```bash
python3 pyGetSystemUpTime.py

# ('000', '000', '001', '00', '05', '53', '923530')
# 000 Years, 000 Months, 001 Days, 00 Hours, 05 Minutes, 53 Seconds, 923530 MicroSeconds.
# 000 Years, 000 Months, 001 Days, 00 Hours, 05 Minutes, 53 Seconds, 923530 MicroSeconds.
```

## [pyHeaderMac.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyHeaderMac.py)
* Generate a standard python header

```bash
python3 pyHeaderMac.py      

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.6 (21G115) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.8 ('v3.10.8:aaaf517424', 'Oct 11 2022 10:14:40')
# Created By  : jayrizzo
# Created Date: Sat Dec 31 12:18:45 2022 CST
# Last ModDate: Sat Dec 31 12:18:45 2022 CST
# =============================================================================
# Notes:
# =============================================================================
```

## [pyImageDownloader.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyImageDownloader.py)
* Easily Download images from other sites.  * Supports (JPG/JPEG/PNG/TIFF/GIF/)

```bash
python3 pyImageDownloader.py

File was created: /Users/jayrizzo/Pictures/JayRizzoDL/logo-stackoverflow.png
```
Or as an import:

```python3
from pyImageDownloader import ImageDownloader

ImageDownloader("https://stackoverflow.design/assets/img/logos/so/logo-stackoverflow.png")
```


## [pyListChecker.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyListChecker.py)
* Generate a true or false if your list is containing another list.  Needed to prevent iteration problems when looping over lists.

```bash 
python3 pyListChecker.py    

# Examples are as follows:
#    bb = ['test', 'consolidated list should return True']
#    f = ListChecker().main(bb)
#    print(f"{f}")
#    # Returns: (False, ['test', 'consolidated list should return True'])
#    try:
#        aa = ['test', ['another list should return False']]
#        d = ListChecker().main(aa)
#        print(d)
#    except Exception as e:
#        print(f"{e}")
#        # Returns: (True, ['test', ['another list should return False']], ERROR: This List Contains Another list Please Fix the list & try again!)
#        exit()
#
#(False, ['test', 'consolidated list should return True'])
#(True, ['test', ['another list should return False']], ERROR: This List Contains Another list Please Fix the list & try again!)
```

## [pyMacOsName.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyMacOsName.py)
* Generate your Mac Operating System Name.  Using `sw_vers` into python variables.

```python3 pyMacOsName.py

# ('macOS', 'Monterey', '12.6', '21G115')
#
# Product Type        : macOS
# Product Name        : Monterey
# Product Version     : 12.6
# Product Build Number: 21G115
# 
# Os Name for 11.4:           Big Sur
# Os Name for 11.04:          Big Sur
# Os Name for 11.14:          Big Sur
# Os Name for 10.02:          X Jaguar
# Os Name for 10.9:           X Mavericks
# Os Name for 10.09.424.24:   X Mavericks
# Os Name for 11.4:           Big Sur
# Os Name for 11.4.2:         Big Sur
# Os Name for 75.02:          ('',)
```

# Shell
This is a bash script to download the google fonts to your current working directory

### [GoogleFontList.sh](https://github.com/JayRizzo/JayRizzoTools/blob/master/GoogleFontList.sh)
* Easily download 1200 fonts from google just by calling this file from the terminal.  Downloads to current working directory.

- [x] Contains Most of the current Known URL's for Google Fonts.
- [x] Uses `curl` to download the zip files.
- [x] Uses `unzip` to Unzip the files into your current working directory.
- [ ] This Does not automatically install the font files, must run info below:

#### Mac Install

> 1. `mkdir ~/Downloads/Fonts`
> 1. `mkdir ~/Downloads/GoogleFonts`
> 1. `cd ~/Downloads/GoogleFonts`
> 1. `bash GoogleFontList.sh`
>    1. Wait for downloads to complete
> 1. Show all Fonts in current Directory & SubDirectories

```bash
# Show all Fonts in current Directory & SubDirectories
find . -name '*.otf'  ## OpenType® font
find . -name '*.ttf'  ## TrueType® font
find . -name '*.ttc'  ## TrueType® font collection
```

> 6. Move all Fonts from Directory & SubDirectories >> into Download Fonts Folder

```bash
# Move all Fonts from Directory & SubDirectories >> into Download Fonts Folder
find -s . -type f -name "*.otf" -exec cp {} ~/Downloads/Fonts \; -print
find -s . -type f -name "*.ttf" -exec cp {} ~/Downloads/Fonts \; -print
find -s . -type f -name "*.ttc" -exec cp {} ~/Downloads/Fonts \; -print
```

> 7. Move all Fonts from Download Fonts Folder >> into ~/Library/Fonts/

```bash
# Move all Fonts from Download Fonts Folder >> into ~/Library/Fonts/
find -s ~/Downloads/Fonts -type f -name "*.otf" -exec cp {}  ~/Library/Fonts/ \; -print
find -s ~/Downloads/Fonts -type f -name "*.ttf" -exec cp {}  ~/Library/Fonts/ \; -print
find -s ~/Downloads/Fonts -type f -name "*.ttc" -exec cp {}  ~/Library/Fonts/ \; -print
```

> 8. `open /System/Applications/Font\ Book.app`
>    1. Wait for system to recognize the new fonts.
>    1. Right Click on Font Name
>    1. Select `Resolve Duplicates`
>    1. Wait for system to recognize the Duplicate fonts & Display Dialog Box.
>    1. Select `Resolve Automatically` Wait for another popup.
>    1. When Asked to move duplicates to TRASH -> Select `OK`

### Complete. You now have over a Thousand New Font Variations.
