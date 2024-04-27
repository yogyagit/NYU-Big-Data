#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
max_word = None
max_count = 0

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
            # check if the current word has a higher count than the previous maximum
            if current_count > max_count:
                max_word = current_word
                max_count = current_count
        current_count = count
        current_word = word

if current_word == word:
    print('%s\t%s' % (current_word, current_count))
    # check if the last word has a higher count than the previous maximum
    if current_count > max_count:
        max_word = current_word
        max_count = current_count

# print the maximum occurring word(s) at the end of the output
if max_word is not None:
    print("Maximum Occurring Word(s): %s\t%s" % (max_word, max_count))
