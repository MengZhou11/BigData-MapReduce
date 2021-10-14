#!/usr/bin/env python
import sys

range = []
range.append([0,20]) #range[0]
range.append([20.01,40]) #range[1]
range.append([40.01,60]) #range[2]
range.append([60.01,80]) #range[3]
range.append([80.01,9999999999]) #range[4]


for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    value = val.split(',')

    try:
        value = float(val[11])
    except ValueError:
        continue

for r in range:
    if r[0]<=value and value<=r[1]:
        print ('%s\t%s' % (str(r[0]),str(r[1])))

    
'''
hjs -D mapreduce.job.reduces=2 -file ~/hw1/task2-a -mapper task2-a/map.py -reducer task2-a/reduce.py -input /mz3043/hw1/task1/task1_out.txt -output /user/mz3043/task2-a.out
'''