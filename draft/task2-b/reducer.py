#!/usr/bin/env python
import sys

count = 0
#read lines from map
for line in sys.stdin:
    if len(line)>1:
        continue

    try:
        value = int(line)
    except ValueError:
        continue

    if value==1:
        count+=1
    
print ('%d' % (count))