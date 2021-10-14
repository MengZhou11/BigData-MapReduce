#!/usr/bin/env python
import sys
from collections import defaultdict

taxi_dict = defaultdict(set)
taxi_count = {}
medallion = None
current_taxi = None

for line in sys.stdin:
    medallion, date = line.strip().split('\t', 1)
    taxi_count[medallion] = taxi_count.get(medallion, 0) + 1
    if date not in taxi_dict[medallion]:
        taxi_dict[medallion].add(date)

for t, date in taxi_dict.items():
    total_trips = taxi_count[t]
    avg_trips = total_trips / len(taxi_dict[t])
    print('%s\t%d,%.2f' % (t, total_trips, avg_trips))