#!/usr/bin/env python
import sys

date = None
prev_date = None
total_revenue = 0.00
total_tolls = 0.00

for line in sys.stdin:
    # extract data
    date, val = line.strip().split('\t', 1)
    revenue, tolls = val.split(',', 1)
    try:
        float_revenue = float(revenue)
        float_tolls = float(tolls)
    except ValueError:
        continue

    if prev_date == date:
        total_revenue += float_revenue
        total_tolls += float_tolls

    else:
        if prev_date:
            print '%s\t%.2f,%.2f' % (prev_date, total_revenue, total_tolls)

        prev_date = date
        total_revenue = float_revenue
        total_tolls = float_tolls

if prev_date == date:
    print '%s\t%.2f,%.2f' % (prev_date, total_revenue, total_tolls)