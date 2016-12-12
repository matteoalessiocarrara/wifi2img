#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Matteo Alessio Carrara <sw.matteoac@gmail.com>

from sys import argv, stdin, stdout

resHoriz, resVert = [int(x) for x in argv[1:3]]

print ("P3 %d %d 100" % (resHoriz, resVert))
pixel = 1
for value in [int(float(x.strip('\n'))) for x in stdin.readlines()]:
	stdout.write((str(value) + " ") * 3 )
	if (pixel % resHoriz) == 0:
		stdout.write("\n")
	else:
		stdout.write(" ")
	pixel += 1
	
