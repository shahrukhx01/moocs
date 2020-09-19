#!/usr/bin/python
import sys
import csv
from collections import Counter


def reducer():
    question = 0
    answers = []
    oldKey = None
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) != 3:
        # Something has gone wrong. Skip this line.
            continue

        id, type, length = line
        length = int(length)

        if oldKey and oldKey != id:
            #some code here...
            print (oldKey, "\t", question, "\t",float(sum(answers)) / max(len(answers), 1))
            oldKey = id;
            question = 0
            answers = []

        oldKey = id
        if type == "answer":
            answers.append(length)
        else:
            question = length

if __name__ == "__main__":
    reducer()
