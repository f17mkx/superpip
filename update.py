#!/usr/bin/env python

import re
import sys
from superpro.saveload import load_file, save_str

if __name__ == "__main__":
    setup_file = load_file('setup.py')
    try:
        new_version = sys.argv[1]
        # new_version = int(new_version[1])
        # new_version = '0.4.31'
        setup_file = re.sub(r'(?<=version=").*\d(?=")', new_version, setup_file)
    except:
        old_version = re.search('version=".*\.(\d*)"',setup_file)[1]
        new_version = str(int(old_version) + 1)
        setup_file = re.sub(r'(?<=version="(\d\.){2})\d+(?=")', new_version, setup_file)

    save_str(setup_file, 'setup.py')
