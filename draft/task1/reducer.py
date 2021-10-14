#!/usr/bin/env python
import sys

old_key = None
key = None
trips_val = []
fares_val = []

for line in sys.stdin:
    # split each line 
    key, val = line.strip().split('\t', 1)
    tag = val.split(',')[0]
    val = ','.join(val.split(',')[1:])

    # if key exists, pair them
    if key == old_key and old_key is not None:
        if tag == 'f':
            fares_val.append(val)
        if tag == 't':
            trips_val.append(val)

    else:
        if (old_key):
                for trips in trips_val:
                    for fares in fares_val:
                        print '%s\t%s' % (old_key, trips + ',' + fares)

        old_key = key
        trips_val = []
        fares_val = []
        if tag == 'f':
            fares_val.append(val)
        if tag == 't':
            trips_val.append(val)

if old_key == key:
        for trips in trips_val:
            for fares in fares_val:
                print '%s\t%s' % (old_key, trips + ',' + fares)