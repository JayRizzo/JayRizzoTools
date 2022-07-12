#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Wed Jun 22 11:34:57 2022 CDT
# Last ModDate: Tue Jul 12 16:36:30 2022 CDT
# =============================================================================
# Notes: Get Your System Running Time 001 Years, 002 Months, 003 Days, 19 Hours, 34 Minutes, 13 Seconds, 570750 MicroSeconds.
# =============================================================================

from uptime import uptime
import time
from psutil import boot_time
import datetime

class GetBootTimeDuration(object):
    """docstring for GetBootTimeDuration
    Input: None
    Output: (self.Years, self.Months, self.Days, self.Hours, self.Minutes, self.Seconds, self.MicroSeconds), self.HumanFormat
    # Example: ((0, 0, 3, 2, 40, 20, 404037), '0 Years, 0 Months, 3 Days, 2 Hours, 40 Minutes, 20.00 Seconds, 404037.000 MicroSeconds.
    """
    def __init__(self):
        super(GetBootTimeDuration, self).__init__()
        # Define the constants
        self.SecPerMINUTE = 60
        self.SecPerHOUR = 3600
        self.SecPerDAY = 86400
        self.HumanFormat = ""
        self.TimeDiffEpoch = 0
        self.epochSeconds = 0
        self.STRUNDERSCORE = "__"
        # Return The Human Readable Format Of The Time Since Boot
        self.LastBootDateTimeHumn = datetime.datetime.utcfromtimestamp(boot_time())
        # Return The Human Readable Format Of The Current Date Time
        self.CurrentDateTimeHumn = datetime.datetime.utcfromtimestamp(datetime.datetime.now().timestamp())
        # Return The Boot_time In Seconds Since The Epoch
        self.LastBootTimeInEpoch = datetime.datetime.fromtimestamp(boot_time()).timestamp()
        # Return The Current Time In Seconds Since The Epoch
        self.CurrentDatetimeEpoch = datetime.datetime.now().timestamp()
        # Return The Diff In Epoch Seconds. Get The Difference Between The CurrentDatetimeEpoch & LastBootTimeInEpoch Dates.
        self.TimeDiffEpoch = self.CurrentDatetimeEpoch - self.LastBootTimeInEpoch
        self.main()

    def main(self):
        self.epochSeconds = self.TimeDiffEpoch
        # Set Vars by Epoch Differences split by datetime object values
        self.Years        = datetime.datetime.utcfromtimestamp(self.epochSeconds).year - 1970 # Subtract the beginning year from epoch
        self.Years        = f"{self.Years:03d}"  # Format the number to always have THREE digits 000
        self.Months       = datetime.datetime.utcfromtimestamp(self.epochSeconds).month - 1   # Subtract one month for January
        self.Months       = f"{self.Months:03d}"  # Format the number to always have THREE digits 000
        self.Days         = datetime.datetime.utcfromtimestamp(self.epochSeconds).day - 1     # Subtract one day for the first
        self.Days         = f"{self.Days:03d}"  # Format the number to always have THREE digits 000
        self.Hours        = datetime.datetime.utcfromtimestamp(self.epochSeconds).hour
        self.Hours        = f"{self.Hours:02d}"  # Format the number to always have TWO digits 00
        self.Minutes      = datetime.datetime.utcfromtimestamp(self.epochSeconds).minute
        self.Minutes      = f"{self.Minutes:02d}"  # Format the number to always have TWO digits 00
        self.Seconds      = datetime.datetime.utcfromtimestamp(self.epochSeconds).second
        self.Seconds      = f"{self.Seconds:02d}"  # Format the number to always have TWO digits 00
        self.MicroSeconds = datetime.datetime.utcfromtimestamp(self.epochSeconds).microsecond
        self.MicroSeconds = f"{self.MicroSeconds:06d}"  # Format the number to always have six digits 000000
        self.HumanFormat  = f"{self.Years} Years, {self.Months} Months, {self.Days} Days, {self.Hours} Hours, {self.Minutes} Minutes, {self.Seconds} Seconds, {self.MicroSeconds} MicroSeconds."
        return (self.Years, self.Months, self.Days, self.Hours, self.Minutes, self.Seconds, self.MicroSeconds), self.HumanFormat

if __name__ == '__main__':
    a = GetBootTimeDuration()
    print(f"{a.main()[0]}")  # ('000', '000', '005', '01', '12', '31', '079742')
    print(f"{a.main()[1]}")  # 000 Years, 000 Months, 005 Days, 01 Hours, 12 Minutes, 31 Seconds, 079742 MicroSeconds.
    print(f"{a.HumanFormat}")
    # print(f"Dir: {[x for x in dir(GetBootTimeDuration()) if GetBootTimeDuration().STRUNDERSCORE not in x]}")
    # print(f"         a.HumanFormat: {a.HumanFormat}")
    # print(f"                     a: {a}")
    # print(f"                a.main: {a.main()}")
    # print(f"a.LastBootDateTimeHumn: {a.LastBootDateTimeHumn}")
    # print(f" a.CurrentDateTimeHumn: {a.CurrentDateTimeHumn}")
    # print(f" a.LastBootTimeInEpoch: {a.LastBootTimeInEpoch}")
    # print(f"a.CurrentDatetimeEpoch: {a.CurrentDatetimeEpoch}")
    # print(f"               a.Years: {a.Years}")
    # print(f"              a.Months: {a.Months}")
    # print(f"                a.Days: {a.Days}")
    # print(f"               a.Hours: {a.Hours}")
    # print(f"             a.Minutes: {a.Minutes}")
    # print(f"             a.Seconds: {a.Seconds}")
    # print(f"        a.MicroSeconds: {a.MicroSeconds}")
    # print(f"           a.SecPerDAY: {a.SecPerDAY}")
    # print(f"          a.SecPerHOUR: {a.SecPerHOUR}")
    # print(f"        a.SecPerMINUTE: {a.SecPerMINUTE}")
    # print(f"       a.TimeDiffEpoch: {a.TimeDiffEpoch}")
