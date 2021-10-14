#!/usr/bin/env python
import sys

for line in sys.stdin:
    key, val = line.strip().split('\t', 1)
    k = key.split(',')

    medallion = k[0]
    license = k[1]

    print ('%s\t%s' % (license, medallion))