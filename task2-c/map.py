#!/usr/bin/env python
import sys

for line in sys.stdin:
    # extract data
    key = None
    k, val = line.strip().split('\t',1)

    # passenger_count
    try:
        key = int(val.split(',')[3])
    except ValueError:
        continue

    # print
    print ('%s' % (key))