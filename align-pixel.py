#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Matteo Alessio Carrara <sw.matteoac@gmail.com>
# Trasforma una scansione a "z" in una a linee 

from sys import argv, stdin, stdout


resHoriz = int(argv[1])
count = 0
buf = []
for val in stdin.readlines():
	buf.append(val)
	if ((count + 1) % resHoriz) == 0:
		if ((count + 1) / resHoriz)  % 2 == 0:
			buf.reverse()
		for v in buf:
			stdout.write(v)
		buf.clear()
	count += 1
