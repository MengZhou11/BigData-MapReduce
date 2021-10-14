#!/usr/bin/env python
import sys

for line in sys.stdin: 
    #skip the first row
    line = line.strip() #rm empty before and after
    if len(line) <=1 or 'medallion' in line: 
        continue
    #split each row
    data = line.split(',')
    
    #for data in fares
    if len(data) ==11:
	    key = ','.join(data[0:4])
  	    val = ','.join(data[4:])
	    print '%s\tf,%s' % (key, val) #give f as tag

    #for data in trips
    elif len(data) ==14:
	    k = ','.join(data[0:3])
	    key = k+','+data[5]
	    val = ','.join(data[3:5]+data[6:])
  	    print '%s\tt,%s' %(key, val) #give t as tag