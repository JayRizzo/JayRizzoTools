#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 21F79
# Created Plat: Python 3.9.5 ('v3.9.5:0a7dcbdb13', 'May  3 2021 13:17:02')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 15:22:59 2022 CDT
# Last ModDate: Sat Jun 18 15:54:47 2022 CDT
# =============================================================================
# Notes: Version 3: Final
# =============================================================================

import subprocess
from os import linesep

class MacOSName(object):
    """Setup INIT for MacOSName.
    `self.macOS` List was Derived From: https://apple.stackexchange.com/a/334337/55628

    This takes the "Major" & "Minor" Versions to generate the name of the Operating System from your mac.
    Gathers the information from ` sw_vers ` and parsed it to derive the version number then loops thru the dict.
    if found version: you will get a name back if not it will return an empty string.

    ## getCurrentSystemInfo:
    Input:
        self
    Output:
        TUPLE('macOS', 'Monterey', '12.4', '21F79')
    Not Found Returns:
        tuple(('',))

    ## getOsName:
    Input:
        str('12.4')
        set({'12.4',})
    Output:
        TUPLE('Monterey')
    Not Found Returns:
        tuple(('',))




    ### Example Usage
    print(f"{MacOSName().getCurrentSystemInfo()}")  # Returns TUPLE('macOS', 'Monterey', '12.4', '21F79')
    a = MacOSName().getCurrentSystemInfo()
    pt = a[0] # Product Type
    pn = a[1] # Product Name
    pv = a[2] # Product Version
    pb = a[3] # Product Build Number
    print(f\"\"\"
    Product Type        : {pt}
    Product Name        : {pn}
    Product Version     : {pv}
    Product Build Number: {pb}
    \"\"\")
    # Product Type        : macOS
    # Product Name        : Monterey
    # Product Version     : 12.4
    # Product Build Number: 21F79

    # # Supports String Versions
    print(f"{MacOSName().getOsName('11.4')}")               # Returns Name  Big Sur
    print(f"{MacOSName().getOsName('11.04')}")              # Returns Name  Big Sur
    print(f"{MacOSName().getOsName('11.14')}")              # Returns Name  Big Sur
    print(f"{MacOSName().getOsName('10.02')}")              # Returns Name  Mojave
    print(f"{MacOSName().getOsName('10.9')}")               # Returns Name  X Mavericks
    print(f"{MacOSName().getOsName('10.09.424.24')}")       # Returns Name  X Mavericks  (ignores any subversion)
    # # Supports Sets Versions
    print(f"{MacOSName().getOsName(set({'11.4'}))}")        # Returns Name  Big Sur
    print(f"{MacOSName().getOsName(set({'11.4.2'}))}")      # Returns Name  Big Sur
    """
    def __init__(self):
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
        self.macOS =            {"12.04" : "Monterey", "12.4" : "Monterey", "12.03" : "Monterey", "12.3" : "Monterey", "12.02" : "Monterey", "12.2" : "Monterey", "12.01" : "Monterey", "12.1" : "Monterey", "12.00" : "Monterey", "12.0" : "Monterey", "11.20" : "Big Sur", "11.19" : "Big Sur", "11.18" : "Big Sur", "11.17" : "Big Sur", "11.16" : "Big Sur", "11.15" : "Big Sur", "11.14" : "Big Sur", "11.13" : "Big Sur", "11.12" : "Big Sur", "11.11" : "Big Sur", "11.10" : "Big Sur", "11.09" : "Big Sur", "11.9" : "Big Sur", "11.08" : "Big Sur", "11.8" : "Big Sur", "11.07" : "Big Sur", "11.7" : "Big Sur", "11.06" : "Big Sur", "11.6" : "Big Sur", "11.05" : "Big Sur", "11.5" : "Big Sur", "11.04" : "Big Sur", "11.4" : "Big Sur", "11.03" : "Big Sur", "11.3" : "Big Sur", "11.02" : "Big Sur", "11.2" : "Big Sur", "11.01" : "Big Sur", "11.1" : "Big Sur", "11.00" : "Big Sur", "11.0" : "Big Sur", "10.20" : "Catalina", "10.19" : "Catalina", "10.18" : "Catalina", "10.17" : "Catalina", "10.16" : "Catalina", "10.15" : "Catalina", "10.14" : "Mojave", "10.13" : "High Sierra", "10.12" : "Sierra", "10.11" : "X El Capitan", "10.10" : "X Yosemite", "10.09" : "X Mavericks", "10.9" : "X Mavericks", "10.08" : "X Mountain Lion", "10.8" : "X Mountain Lion", "10.07" : "X Lion", "10.7" : "X Lion", "10.06" : "X Snow Leopard", "10.6" : "X Snow Leopard", "10.05" : "X Leopard", "10.5" : "X Leopard", "10.04" : "X Tiger", "10.4" : "X Tiger", "10.03" : "X Panther", "10.3" : "X Panther", "10.02" : "X Jaguar", "10.2" : "X Jaguar", "10.01" : "X Puma", "10.1" : "X Puma", "10.0" : "X Cheetah", "10.00" : "X Cheetah"}

    def getOsName(self, verz):
        self.version = verz
        if isinstance(self.version, set):
            self.version    = ''.join(self.version)
            self.major      = self.version.split(".")[0]
            try:
                self.minor  = str(self.version).split(".")[1]
            except IndexError as e:
                self.minor  = 0
            except Exception as e:
                print(f"\n\n\t\t\tSET ERROR: {e}")
            try:
                for j, k in self.macOS.items():
                    self.v = j.split('.')[0]
                    self.m = j.split('.')[1]
                    if self.v == self.major:
                        if self.m == self.minor:
                            self.found = k
                            break
            except Exception as e:
                print(f"\n\n\t\t\tERROR: {e}")

        elif isinstance(self.version, str):
            self.version    = ''.join(self.version)
            self.major      = self.version.split(".")[0]
            try:
                self.minor  = str(self.version).split(".")[1]
            except IndexError as e:
                self.minor  = 0
            except Exception as e:
                print(f"\n\n\t\t\tSTRING ERROR: {e}")
            try:
                for j, k in self.macOS.items():
                    self.v = j.split('.')[0]
                    self.m = j.split('.')[1]
                    if self.v == self.major:
                        if self.m == self.minor:
                            self.found = k
                            break
            except Exception as e:
                print(f"\n\n\t\t\tERROR: {e}")
        return self.found

    def getCurrentSystemInfo(self):
        self.p =              subprocess.Popen("/usr/bin/sw_vers", shell=True, stdout=subprocess.PIPE)
        self.result =         self.p.communicate()[0]
        self.result =         self.result.decode("utf-8").split(str('\t'))
        self.productName =    self.result[1].split(linesep)[0]
        self.productVersion = self.result[2].split(linesep)[0]
        self.buildVersion =   self.result[3].split(linesep)[0]
        self.oSNameFrmVer =   self.getOsName({'12.4'})
        self.productName =    self.result[1].split('\n')[0]
        return self.productName, self.oSNameFrmVer, self.productVersion, self.buildVersion

    def main(self):
        return

if __name__ == '__main__':
    print(f"""# MacOSName().getCurrentSystemInfo()\n# Returns: {MacOSName().getCurrentSystemInfo()}""")
    print("# But, you can parse it out like so.")
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
    print("""\n# Other Example Usages:\n\t# Supports String Versions\n\tprint(f"{MacOSName().getOsName('11.4')}")\n\n\t# Returns Name:""", end="")
    print(f"\t{MacOSName().getOsName('11.4')}")




