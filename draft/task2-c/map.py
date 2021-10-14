#!/usr/bin/env python
import sys

for line in sys.stdin:
    # extract data
    key = None
    val = line.strip()

    # passenger_count
    try:
        key = int(val.split(',')[3])
    except ValueError:
        continue

    # print
    print ('%s' % (key))