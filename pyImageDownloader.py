#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff    
# Created Date: Thu Jun 15 23:31:01 2022 CDT
# Last ModDate: Fri Jul  1 13:31:07 2022 CDT
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
import warnings

a = join(expanduser('~')+ "/Desktop/")

class ImageDownloader(object):
    """URL ImageDownloader.
    Input : Full Image URL
    Output: Image saved to your ~/Pictures/JayRizzoDL folder.
    """
    def __init__(self, URL, CUSTOMOUTFILEFOLDERPATH: str or None = None):
        super(ImageDownloader, self).__init__()
        self.modulename = "pyImageDownloader.py"
        self.url = URL
        self.headers = {"User-Agent" : UA().random}
        self.currentHome = expanduser('~')
        self.desktop = join(self.currentHome + "/Desktop/")
        self.download = join(self.currentHome + "/Downloads/")
        self.pictures = join(self.currentHome + "/Pictures/JayRizzoDL/")
        self.filename = self.getFileNameFromURL()
        self.CustomOutFileFolderPath = join(CUSTOMOUTFILEFOLDERPATH + "" + self.filename)
        self.response = ""
        self.rawstream = ""
        self.imgFileName = self.getFileNameFromURL()
        self.outfile = join(self.pictures, self.imgFileName)
        self.createdfilepath = ""
        # Check if the JayRizzoDL exists in the pictures folder, if it doesn't exist create it.
        if not filepathexist(self.pictures):
            os.mkdir(self.pictures)
        self.main()

    def getFileNameFromURL(self):
        """Parse the URL for the name after the last forward slash."""
        # self.url = URL
        if self.url is not None and self.url != "":
            self.filename = self.url.strip().split('/')[-1].strip()
        return self.filename

    def getResponse(self):
        """Try streaming the URL for the raw data."""
        if self.url is not None and self.url != "":
            self.response = requests.get(self.url, headers=self.headers, stream=True)
        else:
            warnings.warn(message=f"ImageDownloader.getResponse(): No URL Was Provided: self.url: {self.url}", category=None, stacklevel=1, source=None)
        return self.response

    def goCreateFile(self, name: str, response, CustomOutFileFolderPath: str or None = None):
        """Try creating the file with the raw data in a custom folder."""
        self.response = self.getResponse().raw
        self.outfile = self.CustomOutFileFolderPath
        print(f"2. self.outfile: {self.outfile}")
        # print(f"2. self.response: {self.response}")
        with open(self.outfile, 'wb') as outFilePath:
            shutil.copyfileobj(self.response, outFilePath)
        return self.outfile

    def main(self):
        """Combine Everything and use in for loops.
        """
        # print(f"self.url: {self.url}")
        if self.url is None or self.url == "":
            exit(f"self.url2: {self.url}")
        else:
            Exception("ImageDownloader.main(): No URL Was Provided. Exiting")
        self.outfile = self.CustomOutFileFolderPath
        print(f"self.CustomOutFileFolderPath: {self.CustomOutFileFolderPath}")
        print(f"self.CustomOutFileFolderPath: {type(self.CustomOutFileFolderPath)}")
        print(f"self.outfile: {self.outfile}")
        self.imgFileName = self.filename
        self.rawstream = self.getResponse()
        self.createdfilepath = self.goCreateFile(self.filename, self.rawstream, self.outfile)
        print(f"File was created: {self.createdfilepath}")
        return self.createdfilepath

if __name__ == '__main__':
    a = ImageDownloader(URL="https://stackoverflow.design/assets/img/logos/so/logo-stackoverflow.png", CUSTOMOUTFILEFOLDERPATH="/Users/jayrizzo/Desktop/")
    # you can also call like this as well from terminal.
    # python3.12 pyImageDownloader.py "https://stackoverflow.design/assets/img/logos/so/logo-stackoverflow.png" '/Users/jayrizzo/Desktop'
