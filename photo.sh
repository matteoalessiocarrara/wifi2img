#!/bin/bash
# Copyright 2016 Matteo Alessio Carrara <sw.matteoac@gmail.com>

set -e -u

if [[ $# -ne 3 ]]; then
	echo "Uso: photo.sh sampling-rate res-horiz res-vert"
	exit 1
else
	smpRate=$1
	resHoriz=$2
	resVert=$3
fi

./scanner.py $smpRate $resHoriz $resVert | ./align-pixel.py $resHoriz | ./gen-img.py $resHoriz $resVert
