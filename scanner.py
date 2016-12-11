#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Matteo Alessio Carrara <sw.matteoac@gmail.com>

from os import system
from time import sleep
from sys import argv, stderr


smpRate, resHoriz, resVert = [int(x) for x in argv[1:4]]

for i in range(resHoriz * resVert):
	stderr.write(str(i + 1) + "\n")
	system("awk 'NR==3 {print $3}' /proc/net/wireless")
	sleep(smpRate)
