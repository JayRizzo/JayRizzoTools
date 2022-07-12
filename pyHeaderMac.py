#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 03:22:59 2022 CDT
# Last ModDate: Fri Jul  1 13:31:07 2022 CDT
# =============================================================================
# Notes:
# =============================================================================

from datetime import datetime, timezone
import platform
from pyMacOsName import MacOSName
from getpass import getuser

def prPyHeader():
    a = MacOSName().getCurrentSystemInfo()
    print(f"""#!/usr/bin/env python3
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
