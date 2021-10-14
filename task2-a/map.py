#!/usr/bin/env python
import sys

for line in sys.stdin:
    key, val = line.strip().split('\t')
    value = val.split(',')
    v = value[11]

    try:
        v = float(v)
    except ValueError:
        continue
    print('%.2f' % (v))
    
