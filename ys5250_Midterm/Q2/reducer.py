#!/usr/bin/env python

import sys

curr_key = None
curr_values = []

for line in sys.stdin:
    line = line.strip()

    # Parsing the input
    key, val = line.split('\t')
    source, index, value = val.split(',')[0], int(val.split(',')[1]), int(val.split(',')[2])

    # If the key changes, calculate the result and emit
    if key != curr_key:
        if curr_key:
            # Accumulate products and give the result
            source_dict = {}
            result = 0
            for src_type, src_index, src_value in curr_values:
                if src_index in source_dict.keys():
                    source_dict[src_index] *= src_value
                else:
                    source_dict[src_index] = src_value
            res = 0
            for m in source_dict:
                res += source_dict[m]
            print 'R,%s,%s,%d' % (cur_row, cur_col, res)
        curr_key = key
        cur_row, cur_col = map(int, curr_key.split(','))
        curr_values = []

    # Collect products
    curr_values.append((source, index, value))

# Give the last result
if curr_key:
    result = 0
    source_dict = {}
    for src_type, src_index, src_value in curr_values:
        if src_index in source_dict.keys():
            source_dict[src_index] *= src_value
        else:
            source_dict[src_index] = src_value
    res = 0
    for s in source_dict:
        res += source_dict[s]
    print 'R,%s,%s,%d' % (cur_row, cur_col, res)
