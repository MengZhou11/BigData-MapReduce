#!/usr/bin/env python
import sys

total = 0
for line in sys.stdin:
    count = line.strip()
    
    try:
        count = int(count)
    except ValueError:
        continue
    total += count

print ("%d" %(total))