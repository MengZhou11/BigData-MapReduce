#!/usr/bin/env python
import sys

# construct count list
count = []
i = 0
while i < 100:
    count.append(0)
    i += 1

for line in sys.stdin:
    # extract data key is the key from map, val is 1
    l = line.strip()

    #get passenger number from key
    try:
        key = int(l)
    except ValueError:
        continue

    # count increase
    count[key] += 1


# print each passenger number and it's count
for idx in range(100):
    if count[idx] > 0:
        print ('%s\t%d' % (idx, count[idx]))

