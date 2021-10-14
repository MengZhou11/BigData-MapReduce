#!/usr/bin/env python
import sys
from collections import defaultdict

dic = defaultdict(set)
for line in sys.stdin:
    key, val = line.strip().split('\t', 1)  #key is lience, val is medallion

    if val not in dic[key]:
        dic[key].add(val)

for k in dic:
    print ('%s\t%d' % (k, len(dic[k])))