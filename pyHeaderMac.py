#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS High Sierra 21.5.0 (17G65)
# Created Plat: Python 3.9.5 ('v3.9.5:0a7dcbdb13', 'May  3 2021 13:17:02')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 03:22:59 2022 CDT
# Last ModDate: Sat Jun 18 15:54:47 2022 CDT
# =============================================================================
# Notes: Final Version
# =============================================================================
from datetime import datetime, timezone
import os
import platform
import sys
import sysconfig
import subprocess
from os.path import exists
import pprint
from rich import print
from pyMacOsNameClass import MacOSName
import getpass

def prPyHeader():
    a = MacOSName().getCurrentSystemInfo()
    print(f"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: {a[0]} {a[1]} {a[2]} ({a[3]})
# Created Plat: Python {platform.python_version()} {platform.python_build()}
# Created By  : {getpass.getuser()}
# Created Date: {datetime.now().strftime('%c')} {datetime.now(timezone.utc).astimezone().tzname()}
# Last ModDate: {datetime.now().strftime('%c')} {datetime.now(timezone.utc).astimezone().tzname()}
# =============================================================================
# Notes:
# =============================================================================
""")

if __name__ == '__main__':
    prPyHeader()

# print(f"dir(platform):                      {dir(platform)}")
# print(f"dir(sys):                           {dir(sys)}")
# print(f"dir(sysconfig):                     {dir(sysconfig)}")
# print(f"os.name                             {os.name}")
# print(f"platform.architecture():            {platform.architecture()}")
# print(f"platform.mac_ver():                 {platform.mac_ver()}")
# print(f"platform.machine():                 {platform.machine()}")
# print(f"platform.node():                    {platform.node()}")
# print(f"platform.platform():                {platform.platform()}")
# print(f"platform.processor():               {platform.processor()}")
# print(f"platform.python_build():            {platform.python_build()}")
# print(f"platform.python_compiler():         {platform.python_compiler()}")
# print(f"platform.python_implementation():   {platform.python_implementation()}")
# print(f"platform.python_version():          {platform.python_version()}")
# print(f"platform.release():                 {platform.release()}")
# print(f"platform.system():                  {platform.system()}")
# print(f"platform.uname():                   {platform.uname()}")
# print(f"platform.version:                   {platform.version()}")
# print(f"sys._framework:                     {sys._framework}")
# print(f"sys.platform                        {sys.platform}")
# print(f"sysconfig.get_platform():           {sysconfig.get_platform()}")

# print("\n"*10)

