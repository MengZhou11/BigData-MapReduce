#!/usr/bin/env python
import sys

#arr to count trips in each range
count = [0,0,0,0,0]

#read lines from map
for line in sys.stdin:
    try:
        val = float(line)
        if 0<=val and  val<=20.00:
            count[0]+=1
        elif 20.01<=val and val <= 40.00:
            count[1]+=1
        elif 40.01<=val and val <= 60.00:
            count[2]+=1
        elif 60.01<=val  and val <= 80.00:
            count[3]+=1
        elif 80.01<=val and val <= float('inf'):
            count[4]+=1
    except ValueError:
        continue

print ('%s\t%d' % ('0,     20', count[0]))
print ('%s\t%d' % ('20.01, 40', count[1]))
print ('%s\t%d' % ('40.01, 60', count[2]))
print ('%s\t%d' % ('60.01, 80', count[3]))
print ('%s\t%d' % ('80.01, infinite', count[4]))

