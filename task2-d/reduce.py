#!/usr/bin/env python
import sys
from collections import defaultdict


dic = {}
for line in sys.stdin:
    key, val = line.strip().split('\t',1)
    value = val.split(',',1)  #value[0] is revenue, 1 is tips
    pick_date = key
    try:
        revenue = float(value[0])
        tips = float(value[1])
    except ValueError:
        continue

    if pick_date in dic:
        dic[pick_date][0] += revenue
        dic[pick_date][1] += tips
    
    if pick_date not in dic:
        dic[pick_date] = [revenue, tips]

for k,v in dic.items():
    print ('%s\t%.2f,%.2f' % (k, v[0], v[1]))

