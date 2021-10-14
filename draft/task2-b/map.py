#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    val = val.split(',')

    try:
        value = float(val[16])
    except ValueError:
        continue


    if value <= 15.00:
            print ('%s' % (1))

    
