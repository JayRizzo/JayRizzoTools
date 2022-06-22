#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 21F79
# Created Plat: Python 3.9.5 ('v3.9.5:0a7dcbdb13', 'May  3 2021 13:17:02')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 15:22:59 2022 CDT
# Last ModDate: Sat Jun 18 15:54:47 2022 CDT
# =============================================================================
# Notes: Version 2 Class
# =============================================================================

import subprocess
from os import linesep

class MacOSName(object):
    """Setup INIT for MacOSName.
    List Derived From: https://apple.stackexchange.com/a/334337/55628

    This takes the "Major" & "Minor" Verisons to generate the name.
    """
    def __init__(self):
        # super(MacOSName, self).__init__()
        self.escappedTab =      str(r'\t'),
        self.version =          "",
        self.productName =      "",
        self.oSNameFrmVer =     "",
        self.productVersion =   "",
        self.buildVersion =     "",
        self.p =                "",
        self.v =                "",
        self.m =                "",
        self.major =            "",
        self.minor =            "",
        self.found =            "",
        self.result =           "",
        self.verz =             "",
        self.macOS =            {"12.04"  : "Monterey",
                                 "12.4"   : "Monterey",
                                 "12.03"  : "Monterey",
                                 "12.3"   : "Monterey",
                                 "12.02"  : "Monterey",
                                 "12.2"   : "Monterey",
                                 "12.01"  : "Monterey",
                                 "12.1"   : "Monterey",
                                 "12.00"  : "Monterey",
                                 "12.0"   : "Monterey",

                                 "11.20"  : "Big Sur",
                                 "11.19"  : "Big Sur",
                                 "11.18"  : "Big Sur",
                                 "11.17"  : "Big Sur",
                                 "11.16"  : "Big Sur",
                                 "11.15"  : "Big Sur",
                                 "11.14"  : "Big Sur",
                                 "11.13"  : "Big Sur",
                                 "11.12"  : "Big Sur",
                                 "11.11"  : "Big Sur",
                                 "11.10"  : "Big Sur",
                                 "11.09"  : "Big Sur",
                                 "11.9"   : "Big Sur",
                                 "11.08"  : "Big Sur",
                                 "11.8"   : "Big Sur",
                                 "11.07"  : "Big Sur",
                                 "11.7"   : "Big Sur",
                                 "11.06"  : "Big Sur",
                                 "11.6"   : "Big Sur",
                                 "11.05"  : "Big Sur",
                                 "11.5"   : "Big Sur",
                                 "11.04"  : "Big Sur",
                                 "11.4"   : "Big Sur",
                                 "11.03"  : "Big Sur",
                                 "11.3"   : "Big Sur",
                                 "11.02"  : "Big Sur",
                                 "11.2"   : "Big Sur",
                                 "11.01"  : "Big Sur",
                                 "11.1"   : "Big Sur",
                                 "11.00"  : "Big Sur",
                                 "11.0"   : "Big Sur",

                                 "10.20" : "Catalina",
                                 "10.19" : "Catalina",
                                 "10.18" : "Catalina",
                                 "10.17" : "Catalina",
                                 "10.16" : "Catalina",
                                 "10.15" : "Catalina",
                                 "10.14" : "Mojave",
                                 "10.13" : "High Sierra",
                                 "10.12" : "Sierra",
                                 "10.11" : "X El Capitan",
                                 "10.10" : "X Yosemite",

                                 "10.09" : "X Mavericks",
                                 "10.9"  : "X Mavericks",
                                 "10.08" : "X Mountain Lion",
                                 "10.8"  : "X Mountain Lion",
                                 "10.07" : "X Lion",
                                 "10.7"  : "X Lion",
                                 "10.06" : "X Snow Leopard",
                                 "10.6"  : "X Snow Leopard",
                                 "10.05" : "X Leopard",
                                 "10.5"  : "X Leopard",
                                 "10.04" : "X Tiger",
                                 "10.4"  : "X Tiger",
                                 "10.03" : "X Panther",
                                 "10.3"  : "X Panther",
                                 "10.02" : "X Jaguar",
                                 "10.2"  : "X Jaguar",
                                 "10.01" : "X Puma",
                                 "10.1"  : "X Puma",
                                 "10.0"  : "X Cheetah",
                                 "10.00" : "X Cheetah",
                    }
        # self.main()

    def getOsName(self, verz):
        self.version = verz
        if isinstance(self.version, set):
            # print(f"SET self.version raw               : {self.version}")
            self.version    = ''.join(self.version)
            # print(f"SET self.version cnv               : {self.version}")
            self.major           = self.version.split(".")[0]
            # print(f"SET Major                          : {self.major}")
            try:
                self.minor       = str(self.version).split(".")[1]
                # print(f"SET Minor                          : {self.minor}")
            except IndexError as e:
                self.minor       = 0
                # print(f"SET Minor                          : {self.minor}")
            except Exception as e:
                print(f"\n\n\t\t\tSET ERROR: {e}")
            try:
                # print(f"SET SEARCHING FOR version1         : {self.major}.{self.minor}")
                # print(f"SET macOS.items()                  : {self.macOS.items()}")
                for j, k in self.macOS.items():
                    # print(f"SET v 1                        : {self.v}")
                    # print(f"SET m 1                        : {self.m}")
                    self.v = j.split('.')[0]
                    self.m = j.split('.')[1]
                    # print(f"SET v 2                        : {self.v}")
                    # print(f"SET m 2                        : {self.m}")
                    # print(f"SET j.v.m 2                    : {j} ~ {self.v}.{self.m}")
                    if self.v == self.major:
                        if self.m == self.minor:
                            self.found = k
                            # print(f"SET self.found                 : {self.found}")
                            # print(f"SET j.v.m 3                    : {j} ~ {self.v}.{self.m}")
                            break
                # print(f"SET Version Major.Minor      : {self.major}.{self.minor}")
            except Exception as e:
                print(f"\n\n\t\t\tERROR: {e}")

        elif isinstance(self.version, str):
            # print(f"STRING self.version                : {self.version}")
            self.version         = ''.join(self.version)
            # print(f"STRING Updated Verson              : {self.version}")
            self.major           = self.version.split(".")[0]
            # print(f"STRING self.major                  : {self.major}")
            try:
                self.minor       = str(self.version).split(".")[1]
                # print(f"STRING Minor                       : {self.minor}")
            except IndexError as e:
                self.minor       = 0
                # print(f"STRING Minor                       : {self.minor}")
            except Exception as e:
                print(f"\n\n\t\t\tSTRING ERROR             : {e}")
            try:
                # print(f"STRING SEARCHING FOR SET Version   : {self.major}.{self.minor}")
                # print(f"macOS.items()                      : {self.macOS.items()}")
                for j, k in self.macOS.items():
                    self.v = j.split('.')[0]
                    self.m = j.split('.')[1]
                    # print(f"STRING {j}   {self.v}.{self.m}")
                    if self.v == self.major:
                        if self.m == self.minor:
                            self.found = k
                            # print(f"STRING self.found          : {self.found}")
                            # print(f"STRING j.v.m               : {j}.{self.v}.{self.m}")
                            break
                # print(f"STRING Version Major.Minor:    {self.major}.{self.minor}")
            except Exception as e:
                print(f"\n\n\t\t\tERROR: {e}")
        return self.found

    def getCurrentSystemInfo(self):
        # print(f"Start:\nself.result             : {self.result}")
        self.p =                          subprocess.Popen("/usr/bin/sw_vers", shell=True, stdout=subprocess.PIPE)
        self.result =                     self.p.communicate()[0]
        self.result =                     self.result.decode("utf-8").split(str('\t'))
        # print(f"self.result2                    : {self.result}")
        # print(f"self.result3                    : {type(self.result)}")
        self.productName =              self.result[1].split(linesep)[0]
        # print(f"productName                     : {self.productName}")
        self.productVersion =           self.result[2].split(linesep)[0]
        # print(f"productVersion                     : {self.productVersion}")
        self.buildVersion =             self.result[3].split(linesep)[0]
        # print(f"buildVersion                       : {self.buildVersion}")
        # print(f"oSNameFrmVer1                      : {self.oSNameFrmVer}")
        self.oSNameFrmVer =             self.getOsName({'12.4'})
        # self.oSNameFrmVer =             self.getOsName(self.productVersion)
        # print(f"oSNameFrmVer2                      : {self.oSNameFrmVer}")
        # print(f"productName1                       : {self.productName}")
        # print(f"productName1                       : {self.result[1]}")
        self.productName =              self.result[1].split('\n')[0]
        # print(f"productName2                       : {self.productName}")
        # self.productName =              self.result[0].split(str(self.escappedTab))
        # print(f"productName3                       : {self.productName}")
        # self.productName =              self.productName.split(str(self.escappedTab))
        # self.productVersion =           self.result[1].split(str(self.escappedTab))[1]
        # self.buildVersion =             self.result[2].split(self.escappedTab)[1]
        # self.oSNameFrmVer =             self.getOsName(self.productVersion)
        # print(f"result:                 {self.result[0].split({self.escappedTab})}")
        # print(f"result:                 {self.result[0].split(self.escappedTab)[1]}")
        # # return Example: ('macOS', 'Monterey', '12.4', '21F79')
        return self.productName, self.oSNameFrmVer, self.productVersion, self.buildVersion

    def main(self):
        # print(f"main called.")
        # print(f"main called.")
        # print(self.getCurrentSystemInfo())
        # print(f"{dir(self)}")
        # print(f"M                       : {self.m}.")
        # print(f"Major                   : {self.major}.")
        # print(f"Minor                   : {self.minor}.")
        # print(f"buildVersion            : {self.buildVersion}.")
        # print(f"escappedTab             : {self.escappedTab}")
        # print(f"found                   : {self.found}")
        # print(f"getOsName               : {self.getOsName}")
        # print(f"main                    : {self.main}")
        # print(f"oSNameFrmVer            : {self.oSNameFrmVer}")
        # print(f"p                       : {self.p}")
        # print(f"productName             : {self.productName}")
        # print(f"productVersion          : {self.productVersion}")
        # print(f"result                  : {self.result}")
        # print(f"v                       : {self.v}")
        # print(f"Product Name:           : {self.productName}")
        # print(f"Product Version:        : {self.productVersion}")
        # print(f"Build Version:          : {self.buildVersion}")
        # print(f"OSName Version:         : {self.oSNameFrmVer}")
        # print(f"macOS                   : {self.macOS}")
        # # print(f"getCurrentSystemInfo    : {self.getCurrentSystemInfo()}")
        return


if __name__ == '__main__':
    print(f"{MacOSName().getCurrentSystemInfo()}")  # Returns TUPLE('macOS', 'Monterey', '12.4', '21F79')
    a = MacOSName().getCurrentSystemInfo()
    pt = a[0] # Product Type
    pn = a[1] # Product Name
    pv = a[2] # Product Version
    pb = a[3] # Product Build Number
    print(f"""
Product Type        : {pt}
Product Name        : {pn}
Product Version     : {pv}
Product Build Number: {pb}
""")
    # Product Type        : macOS
    # Product Name        : Monterey
    # Product Version     : 12.4
    # Product Build Number: 21F79

    # # Supports String Versions
    print(f"{MacOSName().getOsName('11.4')}")       # Returns Name  Big Sur
    print(f"{MacOSName().getOsName('11.04')}")      # Returns Name  Big Sur
    print(f"{MacOSName().getOsName('11.14')}")      # Returns Name  Big Sur
    print(f"{MacOSName().getOsName('10.02')}")      # Returns Name  Mojave
    print(f"{MacOSName().getOsName('10.9')}")       # Returns Name  X Mavericks
    print(f"{MacOSName().getOsName('10.09.424.24')}")      # Returns Name  X Mavericks  (ignores any subversion)
    # # Supports Sets Versions
    print(f"{MacOSName().getOsName(set({'11.4'}))}")       # Returns Name  Big Sur
    print(f"{MacOSName().getOsName(set({'11.4.2'}))}")       # Returns Name  Big Sur

    # Error:
    a = MacOSName().getOsName('75.02')
    print(type(a))
    print(f"{MacOSName().getOsName('75.02')}")      # Returns Name  Mojave


