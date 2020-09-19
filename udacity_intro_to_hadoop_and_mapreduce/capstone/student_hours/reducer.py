#!/usr/bin/python
import sys
import csv
from collections import Counter


def reducer():
    hours = []
    oldKey = None
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) != 2:
        # Something has gone wrong. Skip this line.
            continue

        id, hour = line
        hour = int(hour)

        if oldKey and oldKey != id:
            max = []
            cnt = Counter(hours)
            vals = cnt.most_common(len(hours))
            i = 0
            max.append(vals[0][0])
            for freq in vals:
                if i > 0 and vals[0][1] == freq[1]:
                    max.append(freq[0])
                elif i > 0:
                    break
                i = i + 1

            print (oldKey, "\t", max, "\t",hours)
            oldKey = id;
            hours = []

        oldKey = id
        hours.append(hour)

    if oldKey != None:
        max = []
        cnt = Counter(hours)
        vals = cnt.most_common(len(hours))
        i = 0
        max.append(vals[0][0])
        for freq in vals:
            if i > 0 and vals[0][1] == freq[1]:
                max.append(freq[0])
            elif i > 0:
                break
            i = i + 1
        print( oldKey, "\t", max, "\t",hours)

if __name__ == "__main__":
    reducer()
