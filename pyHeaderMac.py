#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79)
# Created Plat: Python 3.9.5 ('v3.9.5:0a7dcbdb13', 'May  3 2021 13:17:02')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 03:22:59 2022 CDT
# Last ModDate: Sat Jun 18 16:18:41 2022 CDT
# =============================================================================
# Notes: Final Version
# =============================================================================

from datetime import datetime, timezone
import platform
from pyMacOsName import MacOSName
from getpass import getuser

def prPyHeader():
    a = MacOSName().getCurrentSystemInfo()
    print(f"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: {a[0]} {a[1]} {a[2]} ({a[3]}) Kernel: {platform.system()} {platform.release()}
# Created Plat: Python {platform.python_version()} {platform.python_build()}
# Created By  : {getuser()}
# Created Date: {datetime.now().strftime('%c')} {datetime.now(timezone.utc).astimezone().tzname()}
# Last ModDate: {datetime.now().strftime('%c')} {datetime.now(timezone.utc).astimezone().tzname()}
# =============================================================================
# Notes:
# =============================================================================
""")

if __name__ == '__main__':
    prPyHeader()
