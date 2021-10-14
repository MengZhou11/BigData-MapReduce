#!/usr/bin/env python
import sys

for line in sys.stdin:
    key, val = line.strip().split('\t', 1)
    value = val.split(',')
    day = key.split(',')[3][:10] #get date only

    try:
        revenue = float(value[11]) + float(value[12]) + float(value[14])
    except ValueError:
        continue

    try:
        total_tips = float(value[14])
    except ValueError:
        continue

    print ('%s\t%.2f,%.2f' % (day, revenue, total_tips))