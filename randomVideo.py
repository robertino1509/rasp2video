#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import subprocess
import sys


path = sys.argv[1]
files = os.listdir(path)
n = len(files)

print('Element found: ' + str(n))
for file in files:
    print(file)

while True:
    rand=random.randint(0,n-1)
    print('Element random select: ' + files[rand])
    subprocess.call(["omxplayer","-b","-o","local", path + "/" + files[rand]])