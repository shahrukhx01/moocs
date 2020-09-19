#!/usr/bin/python
import sys
import csv
import re


def reducer():
    studs = []
    oldKey = None
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) != 2 or not re.match("^[0-9]+$", line[0]):
        # Something has gone wrong. Skip this line.
            continue

        id, freq = line
        freq = int(freq)

        if oldKey and oldKey != id:
            print (oldKey, "\t",studs)
            oldKey = id;
            studs = []

        oldKey = id
        studs.append(freq)

    if oldKey != None:
        print (oldKey, "\t",studs)

if __name__ == "__main__":
    reducer()
