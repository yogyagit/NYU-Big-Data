#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()

    mat, i, j, val = line.split(',')
    
    # Converting i, j, and value to int format
    i = int(i)
    j = int(j)
    val = int(val)
    
    # Creating key-value pairs for reducer input
    if mat == 'M':
        for m in range(0, 20):  
            print '%d,%d\tM,%d,%d' % (i,m,j,val)
    elif mat == 'N':
        for m in range(0, 20):  
            print '%s,%s\tN,%s,%s' % (m,j,i,val)

