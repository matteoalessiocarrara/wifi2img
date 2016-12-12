#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Matteo Alessio Carrara <sw.matteoac@gmail.com>

from os import system
from time import sleep
from sys import argv, stderr

smpRate = float(argv[1])
resHoriz, resVert = [int(x) for x in argv[2:4]]

for i in range(resHoriz * resVert):
	if (i % resHoriz) == 0:
		stderr.write("***LINEA %d***\n" % (i / resHoriz + 1))
	stderr.write(str(i % resHoriz + 1) + "\n")
	system("awk 'NR==3 {print $3}' /proc/net/wireless")
	sleep(smpRate)
