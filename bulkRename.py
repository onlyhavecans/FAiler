#!/usr/bin/env python
# encoding: utf-8
"""

An example program for renaming lots of files with FAile

Created by bunnyman on 2013/03/19.
Copyright (c) 2013 Bunni.biz. All rights reserved.
"""
import sys
import os
from FAiler import FAile, FAError

RENAME = '{0.userName} - {0.submissionName}.{0.fileType}'

failes = []
for x in sys.argv[1:]:
    try:
        failes.append(FAile(x))
    except FAError as e:
        pass

for faile in failes:
    try:
        faile.clean_reupload()
        os.rename(
            os.path.join(faile.directory, faile.basename),
            os.path.join(faile.directory, RENAME.format(faile))
        )
    except OSError as e:
        print("File {} failed because of {}".format(faile.basename, e))
