#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.9.5 ('v3.9.5:0a7dcbdb13', 'May  3 2021 13:17:02')
# Created By  : Jeromie Kirchoff
# Created Date: Thu Jun 15 23:31:01 2022 CDT
# Last ModDate: Wed Jun 29 23:23:34 2022 CDT
# =============================================================================
# Notes: https://stackoverflow.com/a/72642393/1896134
# Notes: Doesn't work on SVG images at this time.
# Notes: I will look into this further: https://stackoverflow.com/a/6599172/1896134
# =============================================================================

import requests                                 # to get image from the web
import shutil                                   # to save it locally
import os                                       # needed
from os.path import exists as filepathexist     # check if file paths exist
from os.path import join                        # joins path for different os
from os.path import expanduser                  # expands current home
from pyuser_agent import UA                     # generates random UserAgent Header

class ImageDownloader(object):
    """URL ImageDownloader.
    Input : Full Image URL
    Output: Image saved to your ~/Pictures/JayRizzoDL folder.
    """
    def __init__(self, URL: str):
        self.url = URL
        self.headers = {"User-Agent" : UA().random}
        self.currentHome = expanduser('~')
        self.desktop = join(self.currentHome + "/Desktop/")
        self.download = join(self.currentHome + "/Downloads/")
        self.pictures = join(self.currentHome + "/Pictures/JayRizzoDL/")
        self.outfile = ""
        self.filename = ""
        self.response = ""
        self.rawstream = ""
        self.createdfilepath = ""
        self.imgFileName = ""
        # Check if the JayRizzoDL exists in the pictures folder, if it doesn't exist create it.
        if not filepathexist(self.pictures):
            os.mkdir(self.pictures)
        self.main()

    def getFileNameFromURL(self, URL: str):
        """Parse the URL for the name after the last forward slash."""
        NewFileName = self.url.strip().split('/')[-1].strip()
        return NewFileName

    def getResponse(self, URL: str):
        """Try streaming the URL for the raw data."""
        self.response = requests.get(self.url, headers=self.headers, stream=True)
        return self.response

    def gocreateFile(self, name: str, response):
        """Try creating the file with the raw data in a custom folder."""
        self.outfile = join(self.pictures, name)
        with open(self.outfile, 'wb') as outFilePath:
            shutil.copyfileobj(response.raw, outFilePath)
        return self.outfile

    def main(self):
        """Combine Everything and use in for loops."""
        self.filename = self.getFileNameFromURL(self.url)
        self.rawstream = self.getResponse(self.url)
        self.createdfilepath = self.gocreateFile(self.filename, self.rawstream)
        print(f"File was created: {self.createdfilepath}")
        return

if __name__ == '__main__':
    # Example when calling the file directly.
    ImageDownloader("https://stackoverflow.design/assets/img/logos/so/logo-stackoverflow.png")
