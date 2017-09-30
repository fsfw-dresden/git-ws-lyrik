#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import utils


dirs = ["sonnets", "gedichte", "poemas"]
allfiles = []
for d in dirs:
    try:
        files = os.listdir(d)
    except FileNotFoundError:
        continue
    for f in files:
        allfiles.append(os.path.join(d, f))

allfiles.sort(key=utils.fsize)

print("Das kürzeste Gedicht ist {}".format(allfiles[0]))
