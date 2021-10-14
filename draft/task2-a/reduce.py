#!/usr/bin/env python
import sys

#arr to count trips in each range
count = [0,0,0,0,0]

#read lines from map
for line in sys.stdin:
    key, val = line.strip().split('\t') #key = range, val =1
    try:
        if float(key)==0.00 and float(val) == 20.00:
            count[0]+=1
        elif float(key)==20.01 and float(val) == 40.00:
            count[1]+=1
        elif float(key)==40.01 and float(val) == 60.00:
            count[2]+=1
        elif float(key)==60.01 and float(val) == 80.00:
            count[3]+=1
        elif float(key)==80.01 and float(val) == 9999999999.00:
            count[4]+=1
    except ValueError:
        continue

print ('%s\t%d' % ('0,     20', count[0]))
print ('%s\t%d' % ('20.01, 40', count[1]))
print ('%s\t%d' % ('40.01, 60', count[2]))
print ('%s\t%d' % ('60.01, 80', count[3]))
print ('%s\t%d' % ('80.01, infinite', count[4]))

