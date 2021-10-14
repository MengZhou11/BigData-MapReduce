#!/usr/bin/env python
import sys

for line in sys.stdin:
    key, val = line.strip().split('\t', 1)
    s_val = val.split(',')

    day = key.split(',')[3][:10]

    try:
        revenue = float(s_val[11]) + float(s_val[12]) + float(s_val[14])
    except ValueError:
        continue

    try:
        tolls = float(s_val[15])
    except ValueError:
        continue

    print '%s\t%s,%s' % (day, revenue, tolls)