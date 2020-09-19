#!/usr/bin/python
import sys
import csv
from collections import Counter


def reducer():
    freqs = 0
    oldKey = None
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) != 2:
        # Something has gone wrong. Skip this line.
            continue

        id, freq = line
        freq = int(freq)

        if oldKey and oldKey != id:
            print (oldKey, "\t",freqs)
            oldKey = id;
            freqs = 0

        oldKey = id
        freqs+=freq

    if oldKey != None:
        print (oldKey, "\t",freqs)

if __name__ == "__main__":
    reducer()
