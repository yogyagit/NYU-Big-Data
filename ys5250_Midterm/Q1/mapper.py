#!/usr/bin/env python3

import sys
import random

# number of samples input by the user
numSample = int(sys.argv[1])  

reservoir = []

for line in sys.stdin:
    line = line.strip()
    if len(reservoir) < numSample:
        reservoir.append(line)
    else:
        num = random.randint(0, numSample)
        if num < numSample:
            reservoir[num] = line

# emitting results
for sampled_line in reservoir:
    print(sampled_line)
