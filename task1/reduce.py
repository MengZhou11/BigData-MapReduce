#!/usr/bin/env python

from operator import itemgetter
import sys
from datetime import datetime as dt
from csv import reader

curr_trips = []
curr_fares = []
curr_key = None

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t', 1)
        value = value.strip().split(',')
        if curr_key == None:
            curr_key = key
        if curr_key == key:
            if len(value) == 10:
                curr_trips.append(','.join(value))
            elif len(value) == 7:
                curr_fares.append(','.join(value))

        else:
            if curr_key != None:
                for trips in curr_trips:
                    for fares in curr_fares:
                        print('%s\t%s' % (curr_key, trips+','+fares))
            curr_key = key
            curr_trips = []
            curr_fares = []
            if len(value) == 10:
                curr_trips.append(','.join(value))
            elif len(value) == 7:
                curr_fares.append(','.join(value))
    except Exception as e:
        continue

if curr_key == key:
    for trips in curr_trips:
        for fares in curr_fares:
            print('%s\t%s' % (curr_key, trips+','+fares))