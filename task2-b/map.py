#!/usr/bin/env python
import sys

count = 0
for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = value.split(',')

    try:
        total_amount = float(value[16])
    except ValueError as e:
        continue

    if total_amount <= 15.00:
        count += 1
print ('%d' % (count))