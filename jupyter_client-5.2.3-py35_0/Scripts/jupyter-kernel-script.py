#!C:\ci\jupyter_client_1521484351477\_h_env\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'jupyter-client==5.2.3','console_scripts','jupyter-kernel'
__requires__ = 'jupyter-client==5.2.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('jupyter-client==5.2.3', 'console_scripts', 'jupyter-kernel')()
    )
