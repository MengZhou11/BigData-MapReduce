#!/usr/bin/env python
import sys

dic = {}
for line in sys.stdin:
    key, val = line.strip().split('\t')
    value = val.split(',')
    key = key.split(',')

    medallion = key[0]
    date = key[3][:10] #get date only

    print ('%s\t%s' % (medallion, date))