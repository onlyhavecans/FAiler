#!/usr/bin/env python
# encoding: utf-8
"""

An example program for renaming lots of files with FAile

Created by bunnyman on 2013/03/19.
Copyright (c) 2013 Bunni.biz. All rights reserved.
"""
import os
import argparse
from FAiler import FAile, FAError

RENAME = '{0.artist} - {0.name}.{0.fileType}'

parser = argparse.ArgumentParser(description='Rename Files with FAile')
parser.add_argument('file', nargs='+', help="Files to rename")
parser.add_argument('--rename', default=RENAME, nargs=1,
                    help='Optional format string to rename with')
args = parser.parse_args()

failes = []
for x in args.file:
    try:
        failes.append(FAile(x))
    except FAError as e:
        pass

for faile in failes:
    try:
        faile.clean_reupload()
        os.rename(
            os.path.join(faile.directory, faile.filename),
            os.path.join(faile.directory, args.rename.format(faile))
        )
    except OSError as e:
        print("File {} failed because of {}".format(faile.basename, e))
