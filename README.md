# JayRizzoTools
Aggregation of Scripts to make life a bit more interesting.

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
```
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

## [pyGenRandAdverb.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandAdverb.py)
* Generate a Random String containing an Adverb.

## [pyGenRandAnimal.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandAnimal.py)
* Generate a Random String containing an Animal.

## [pyGenRandCompanieName.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandCompanieName.py)
* Generate a Random String containing a random company name.

## [pyGenRandEmoji.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandEmoji.py)
* Generate a Random String containing a random Emoji Character.

## [pyGenRandFontObj.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandFontObj.py)
* Generate a Random String containing a random Font from your Mac Machine.

## [pyGenRandLuckyNumbers.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandLuckyNumbers.py)
* Generate a Random Tuple containing a random set of 6 numbers.

## [pyGenRandHEX.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandHEX.py)
* Generate a Random String containing a random HEX.

## [pyGenRandRGB.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandRGB.py)
* Generate a Random Tuple containing a random set of 6 numbers.

## [pyGenRandStatement.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGenRandStatement.py)
* Generate a Random String containing a random phrase.

## [pyGetSystemUpTime.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyGetSystemUpTime.py)
* Generate your system uptime in a readable format from epoch time.

## [pyHeaderMac.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyHeaderMac.py)
* Generate a standard python header

## [pyImageDownloader.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyImageDownloader.py)
* Easily Download images from other sites.  * Supports (JPG/JPEG/PNG/TIFF/GIF/)

## [pyListChecker.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyListChecker.py)
* Generate a true or false if your list is containing another list.  Needed to prevent iteration problems when looping over lists.

## [pyMacOsName.py](https://github.com/JayRizzo/JayRizzoTools/blob/master/pyMacOsName.py)
* Generate your Mac Operating System Name.  Using `sw_vers` into python variables.



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

