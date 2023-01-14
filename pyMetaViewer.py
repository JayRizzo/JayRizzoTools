#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.6 (21G115) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.8 ('v3.10.8:aaaf517424', 'Oct 11 2022 10:14:40')
# Created By  : jayrizzo
# Created Date: Tue Dec 31 11:10:12 2022 CST
# Last ModDate: Tue Dec 31 21:51:10 2022 CST
# =============================================================================
# Notes:
# =============================================================================
"""Download Youtube Audio by providing the URL."""
import functools  # Reduce - Required for ID3 Header Checks
from os.path import exists as filepathexist
from sys import argv
from os import getcwd
from os.path import dirname
from os.path import join
from os import makedirs
from os.path import expanduser
import PySimpleGUI as sg
from time import sleep
from pyMP3TagEditor import MP3TagYourSong           # Custom Import From This Location
# ========================================================================
# KNOWN ISSUES
# ========================================================================

# ========================================================================
# Research
# ========================================================================
# https://stackoverflow.com/a/58014474/1896134
# https://stackoverflow.com/q/18248200/1896134

# Four Character Imports
# https://pypi.org/project/mutagen/1.45.1/
# https://mutagen.readthedocs.io/en/latest/changelog.html
# https://mutagen.readthedocs.io/en/latest/api/id3_frames.html?highlight=Group%20identification%20registration
#
# ========================================================================
# Load Emoji Characters ==================================================
# ========================================================================
MUSICNOTE = '\U0001F3B5'
THINKINFC = '\U00002795'
CHEQRDFLG = '\U0001F7E2'


class App(object):
    """JayRizzo Youtube Downloader."""
    def __init__(self):
        """JayRizzo Youtube Downloader Initial Launch Setup."""
        super().__init__()
        # ========================================================================
        # ==================== Initialize the SimpleGUI Layout ===================
        # ========================================================================
        self.OS_PATH                = ''
        self.CURRENT_DIR            = dirname(argv[0])
        self.THEME                  = sg.ChangeLookAndFeel('Dark')
        self.OPTION                 = sg.SetOptions (
                                                      background_color = 'Black'
                                                    , element_background_color = 'Grey'
                                                    , text_element_background_color = 'Black'
                                                    , font = ('Arial', 12, 'bold')
                                                    , text_color = 'White'
                                                    , input_text_color = 'White'
                                                    , button_color = (sg.YELLOWS[0], sg.BLUES[1])
                                                    )

        # Set Groups For Layout
        self.row01 = [  sg.T(''                                                                 , expand_x=True, key='-IDTEXT-')]
        self.row02 = [  sg.FileBrowse(f'Select File To View Meta Data {THINKINFC}'              , expand_x=True, key='-ID-')]
        self.row03 = [  sg.B(F'Show Meta {CHEQRDFLG}', button_color=(sg.YELLOWS[0], sg.BLUES[1]), expand_x=True, key='-SHOWMETADATA-'           , size=(20,1))]
        self.row04 = [  sg.T('Title:')     , sg.InputText(''                                    , expand_x=True, key='-TEXT-SONGTITLE-'         , size=(60,1))
                      , sg.T('Duration:')  , sg.InputText(''                                    , expand_x=True, key='-TEXT-SONGDURATIONTIME-'  , size=(5, 1))]
        self.row05 = [  sg.T('Artist:')    , sg.InputText(''                                    , expand_x=True, key='-TEXT-SONGARTIST-'        , size=(60,1))
                      , sg.T('PlayCount:') , sg.InputText(''                                    , expand_x=True, key='-NUMBER-SONGPLAYCOUNT-'   , size=(5, 1))]
        self.row16 = [  sg.T('Album Artist:')     , sg.InputText(''                             , expand_x=True, key='-TEXT-SONGALBUMARTIST-'         , size=(60,1))]
        self.row06 = [  sg.T('Album:')     , sg.InputText(''                                    , expand_x=True, key='-TEXT-SONGALBUM-'         , size=(60,1))]
        self.row07 = [  sg.T('BitRate:')   , sg.InputText(''                                    , expand_x=True, key='-NUMBER-BITRATE-'         , size=(20,1), disabled=True)]
        self.row08 = []
        self.row30 = [ sg.B(f'Save', button_color=(sg.YELLOWS[0], sg.BLUES[1])                  , expand_x=True, key='-SAVEDATA-'               , size=(20,1))]

        # Build Layout
        self.LAYOUT = [
                          self.row01
                        , self.row02
                        , self.row03
                        , self.row04
                        , self.row05
                        , self.row16
                        , self.row06
                        , self.row07
                        , self.row30
                      ]

        # Build Window
        self.WINDOW = sg.Window(F"{MUSICNOTE} JayRizzo's MP3 Meta Data Exposè {MUSICNOTE}"
                                , self.LAYOUT
                                , font = 'Arial 12'
                                , size=(700, 500)
                                , resizable = True
                                , grab_anywhere = False
                                , finalize=True
                                , keep_on_top=True
                                )

    def guiUpdater(self):
        self.SONG = MP3TagYourSong(self.values['-ID-'])
        self.WINDOW['-TEXT-SONGTITLE-'].Update(self.SONG.getSongName())
        self.WINDOW['-TEXT-SONGARTIST-'].Update(self.SONG.getSongArtist())
        self.WINDOW['-TEXT-SONGALBUM-'].Update(self.SONG.getSongAlbum())
        self.WINDOW['-NUMBER-SONGPLAYCOUNT-'].Update(self.SONG.getSongPlayCount())
        self.WINDOW['-TEXT-SONGDURATIONTIME-'].Update(self.SONG.duration_from_seconds(self.SONG.SONGDURATION))
        self.WINDOW['-NUMBER-BITRATE-'].Update(self.SONG.getSongInfoBitrate()[1])
        self.WINDOW['-TEXT-SONGALBUMARTIST-'].Update(self.SONG.getSongAlbumArtist())
        # self.WINDOW['-NUMBER-SONGBPM-'].Update(self.SONG.getSongBPM())
        # self.WINDOW['-NUMBER-SONGDURATIONSEC-'].Update(self.SONG.SongDuration)
        # self.WINDOW['-TEXT-SONGALBUM-'].Update(self.SONG.getSongName())
        print('guiUpdater was called.')
        self.SONG.CreateMissingTag()
        self.SONG.CheckID3Tag()
        self.SONG.convertID3Tags2to3()

    def main(self):
        # Create an self.event loop
        while True:
            self.event, self.values = self.WINDOW.read()
            print(self.event, self.values)
            self.WINDOW['-IDTEXT-'].Update(self.values['-ID-'])

            if self.event == "-SHOWMETADATA-":
                if len(self.values['-ID-']) >= 11:
                    self.guiUpdater()

            if self.event == "-SAVEDATA-":
                    self.SONG = MP3TagYourSong(self.values['-ID-'])
                    self.SONG.setSongTitle(f"{self.values['-TEXT-SONGTITLE-']}")
                    self.SONG.setSongArtist(f"{self.values['-TEXT-SONGARTIST-']}")
                    self.SONG.setSongAlbum(f"{self.values['-TEXT-SONGALBUM-']}")
                    self.SONG.setSongAlbumArtist(f"{self.values['-TEXT-SONGALBUMARTIST-']}")
                    self.SONG.setSongPlayCount(f"{self.values['-NUMBER-SONGPLAYCOUNT-']}")
                    self.guiUpdater()

            if self.event == "-EXITBTN-" or self.event == sg.WIN_CLOSED:
                # END PROGRAM IF USER CLOSES WINDOW
                break

if __name__ == "__main__":
    app = App()
    app.main()

