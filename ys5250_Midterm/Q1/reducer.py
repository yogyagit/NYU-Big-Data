#!/usr/bin/env python3

import sys
import random

# user inputs the reservoir size
numSampleRed = int(sys.argv[1]) 

# initialing empty reservoir
reservoir = []
flag = 0

for line in sys.stdin:
    line = line.strip()
    flag += 1

    if len(reservoir) < numSampleRed:
        reservoir.append(line)
    else:

        numRed = random.randint(0, flag)
        if numRed < numSampleRed:
            reservoir[numRed] = line

for sampled_line_fin in reservoir:
    print(sampled_line_fin)
