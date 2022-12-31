#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.6 (21G115) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.8 ('v3.10.8:aaaf517424', 'Oct 11 2022 10:14:40')
# Created By  : jayrizzo
# Created Date: Tue Dec 27 11:21:26 2022 CST
# Last ModDate: Tue Dec 27 15:51:10 2022 CST
# =============================================================================
# Notes:
# =============================================================================
"""Download Youtube Audio by providing the URL."""
from os.path import exists as filepathexist
from pytube import YouTube
from sys import argv
from os import getcwd
from os.path import dirname                     # Show the Script Path To This Script
from os.path import join                        # Joins folder names by Operating System
from os import makedirs                         # Make the Directories if they don't exist
from os.path import expanduser                  # Gets The Current Users Home Folder
import PySimpleGUI as sg
from time import sleep


# ========================================================================
# KNOWN ISSUES
# ========================================================================
# USE THIS IF FILE STRUCTURE IS NOT REFRESHING QUICKLY
# https://discussions.apple.com/thread/8584001
# ARCHIVE/DELETE ~/Library/Preferences/com.apple.finder.plist THEN while in FINDER app
# Navigate to the APPLE LOGO & HOLD CTRL + SHIFT  Select "Force Quit Finder"

# ========================================================================
# Load Emoji Characters ==================================================
# ========================================================================
MUSICNOTE = '\U0001F3B5'


class App(object):
    """JayRizzo Youtube Downloader."""
    def __init__(self):
        """JayRizzo Youtube Downloader Initial Launch Setup."""
        super().__init__()
        # ========================================================================
        # ==================== Initialize the SimpleGUI Layout ===================
        # ========================================================================
        self.FILETOCONVERT          = ''
        self.OS_PATH                = ''
        self.YTVID_ID               = ''
        self.YTVID_DID              = ''
        self.YOUTUBE_URL            = ''
        self.YOUTUBE_URL_STREAM     = ''
        self.CURRENT_DIR            = dirname(argv[0])
        self.CURRENTHOME            = expanduser('~')
        self.DESKTOP_FOLDER         = join(self.CURRENTHOME, "Desktop")
        self.MUSIC_FOLDER           = join(self.CURRENTHOME, "Music","JayRizzoDL")
        self.VIDEO_FOLDER           = join(self.CURRENTHOME, "Movies","JayRizzoDL")
        self.DOWNLOAD_FILE_PATH     = ''
        self.MENU_DEF = [
                          ['File',
                                    ['Open', 'Save', 'Exit',]
                          ]
                        , ['Edit',
                                    ['Paste',
                                              ['Special', 'Normal',]
                                      , 'Undo'
                                    ],
                          ]
                        , ['Help', 'About...']
                        ]
        self.THEME = sg.ChangeLookAndFeel('Dark')
        self.OPTION = sg.SetOptions (
                                      background_color = 'Black'
                                    , element_background_color = 'Black'
                                    , text_element_background_color = 'Black'
                                    , font = ('Arial', 12, 'bold')
                                    , text_color = 'White'
                                    , input_text_color = 'White'
                                    , button_color = ('SkyBlue', 'SkyBlue')
                                    )
        self.BOX_FRAME_LAYOUT = [
                                    [sg.T('Download Folder Locations:')]
                                  , [sg.Text(f"MUSIC FOLDER: {self.MUSIC_FOLDER}", key='-MUSICFOLDERTEXT-', font='Consolas 11')]
                                  , [sg.Text(f"VIDEO FOLDER: {self.VIDEO_FOLDER}", key='-VIDEOFOLDERTEXT-', font='Consolas 11')]
                                  # , [sg.T('Other Folder Locations:')]
                                  # , [sg.Text(f"DESKTOP FOLDER: {self.DESKTOP_FOLDER}", key='-DESKTOPFOLDERTEXT-', font='Consolas 11')]
                                  # , [sg.Text(f"SCRIPT PATH:  {self.CURRENT_DIR}", key='-SCRIPTFOLDERTEXT-', font='Consolas 11')]
                                  # , [sg.Text(f"CURRENT HOME PATH:  {self.CURRENTHOME}", key='-CURRENTHOMEFOLDERTEXT-', font='Consolas 11')]
                                ]

        self.row1 = [sg.T('Enter YouTube URL'), sg.In(key='-ID-', expand_x=True)]
        self.row2 = [ sg.B('Download Audio', button_color=(sg.YELLOWS[1], sg.BLUES[1]), key='-DLAUDIOBTN-', size=(20,1), expand_x=True)
                          , sg.VSep()
                          , sg.B('Download Video', button_color=(sg.YELLOWS[1], sg.BLUES[1]), key='-DLVIDEOBTN-', size=(20,1), expand_x=True)
                          ]
        self.row3 = [ sg.B('Clear Text', button_color=(sg.YELLOWS[1], sg.BLUES[1]), key='-CLRTXTBTN-', size=(20,1), expand_x=True)
                          , sg.VSep()
                          , sg.B('Exit', button_color=(sg.YELLOWS[1], sg.BLUES[1]), key='-EXITBTN-', size=(20,1), expand_x=True)]
        self.row4 = [sg.Text('EXAMPLE URL: https://www.youtube.com/watch?v=3k76FCjHKUM    The extra URL &params= do not cause issues.\n                   OR:          3k76FCjHKUM          Both options will work.', key='-DISPLAYTEXT-')]
        self.row5 = [sg.Frame('Info', self.BOX_FRAME_LAYOUT, element_justification='center', font='Consolas 22', title_color='SkyBlue', size=(250,80), expand_x=True, expand_y=True)]
        self.LAYOUT = [
                          self.row1
                        , self.row2
                        , self.row3
                        , self.row4
                        , self.row5
                      ]
        self.WINDOW = sg.Window(F"{MUSICNOTE} JayRizzo's Youtube Downloader {MUSICNOTE}"
                                , [[sg.Menu(self.MENU_DEF)], self.LAYOUT]
                                , font = 'Arial 12'
                                , size=(700, 280)
                                , resizable = True
                                , grab_anywhere = False
                                , finalize=True
                                , keep_on_top=True  # https://stackoverflow.com/a/58014474/1896134
                                )

    def downloadYouTubeAudio(self, videourl):
        self.YOUTUBE_URL = YouTube(videourl)
        videourl = None
        print(self.YOUTUBE_URL.title)
        print(self.YOUTUBE_URL.author)
        self.YOUTUBE_URL_STREAM = self.YOUTUBE_URL.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
        if not filepathexist(self.MUSIC_FOLDER):
            makedirs(self.MUSIC_FOLDER)
        self.DOWNLOAD_FILE_PATH = self.YOUTUBE_URL_STREAM.download(output_path=self.MUSIC_FOLDER)
        print(f"self.DOWNLOAD_FILE_PATH:    {self.DOWNLOAD_FILE_PATH}")
        return self.DOWNLOAD_FILE_PATH

    def downloadYouTubeVideo(self, videourl):
        self.YOUTUBE_URL = YouTube(videourl)
        videourl = None
        self.YOUTUBE_URL_STREAM = self.YOUTUBE_URL.streams.filter(only_audio=False, progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not filepathexist(self.VIDEO_FOLDER):
            makedirs(self.VIDEO_FOLDER)
        self.DOWNLOAD_FILE_PATH = self.YOUTUBE_URL_STREAM.download(output_path=self.VIDEO_FOLDER)
        print(f"self.DOWNLOAD_FILE_PATH:    {self.DOWNLOAD_FILE_PATH}")
        return self.DOWNLOAD_FILE_PATH

    def clear_last_values(self):
        self.WINDOW['-ID-'].Update('')
        self.YOUTUBE_URL = None
        self.YOUTUBE_URL_STREAM = None
        self.DOWNLOAD_FILE_PATH = None

    def main(self):
        # Create an self.event loop
        while True:
            self.event, self.values = self.WINDOW.read()
            if self.event == "-DLAUDIOBTN-":
                self.WINDOW['-DISPLAYTEXT-'].Update(f"Starting The Audio Download")
                sleep(0.5)
                if len(self.values['-ID-']) == 11 and self.values['-ID-'] != 'DISPLAYTEXT':
                    self.YTVID_ID = self.values['-ID-']
                    b = "https://www.youtube.com/watch?v="
                    c = b + self.YTVID_ID
                    try:
                        self.DOWNLOAD_FILE_PATH = self.downloadYouTubeAudio(c)
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"My Downloaded Song: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                    except FileExistsError as e:
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"Song Has Already Been Downloaded: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                    except RegexMatchError as e:
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"Something Went Wrong With the URL: {self.values['-ID-']}")
                        self.clear_last_values()
                elif len(self.values['-ID-']) > 11 and '?v=' in self.values['-ID-']:
                    self.YTVID_ID = self.values['-ID-']
                    self.YTVID_DID = self.YTVID_ID.split('?v=')[1]
                    b = "https://www.youtube.com/watch?v="
                    c = b + self.YTVID_DID
                    try:
                        self.DOWNLOAD_FILE_PATH = self.downloadYouTubeAudio(c)
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"My Downloaded Song: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                    except FileExistsError as e:
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"Song Has Already Been Downloaded: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                else:
                    self.WINDOW['-ID-'].Update('')
                    self.WINDOW['-DISPLAYTEXT-'].Update(f"The URL is Invalid: {self.values['-ID-']}")
                    self.clear_last_values()

            if self.event == "-DLVIDEOBTN-":
                self.WINDOW['-DISPLAYTEXT-'].Update(f"Starting The Video Download : {self.values}")
                sleep(0.5)
                if len(self.values['-ID-']) == 11 and self.values['-ID-'] != 'DISPLAYTEXT':
                    self.YTVID_ID = self.values['-ID-']
                    b = "https://www.youtube.com/watch?v="
                    c = b + self.YTVID_ID
                    try:
                        self.DOWNLOAD_FILE_PATH = self.downloadYouTubeVideo(c)
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"My Downloaded Video: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                    except FileExistsError as e:
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"Video Has Already Been Downloaded: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                elif len(self.values['-ID-']) > 11 and '?v=' in self.values['-ID-']:
                    self.YTVID_ID = self.values['-ID-']
                    self.YTVID_DID = self.YTVID_ID.split('?v=')[1]
                    b = "https://www.youtube.com/watch?v="
                    c = b + self.YTVID_DID
                    try:
                        self.DOWNLOAD_FILE_PATH = self.downloadYouTubeVideo(c)
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"My Downloaded Video: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                    except FileExistsError as e:
                        self.WINDOW['-DISPLAYTEXT-'].Update(f"Video Has Already Been Downloaded: {self.DOWNLOAD_FILE_PATH}")
                        self.clear_last_values()
                else:
                    self.WINDOW['-ID-'].Update('')
                    self.WINDOW['-DISPLAYTEXT-'].Update(f"The URL is Invalid: {self.values['-ID-']}")
                    self.clear_last_values()

            if self.event == "-CLRTXTBTN-":
                self.WINDOW['-ID-'].Update('')
                self.WINDOW['-DISPLAYTEXT-'].Update('')

            if self.event == "-EXITBTN-" or self.event == sg.WIN_CLOSED:
                # END PROGRAM IF USER CLOSES WINDOW
                break

if __name__ == "__main__":
    app = App()
    app.main()
