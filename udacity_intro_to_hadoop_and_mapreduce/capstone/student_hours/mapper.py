#!/usr/bin/python
import sys
import csv
from datetime import *
from itertools import groupby as g
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
        if len(added_at.split(" "))==2:
            writer.writerow((author_id,int(added_at.split(" ")[1].split(":")[0])))

if __name__ == "__main__":
    mapper()
